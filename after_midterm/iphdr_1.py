# 필요한 모듈을 가져옵니다.
import socket, struct, binascii

class Iphdr:
    # IP 헤더 클래스 초기화
    def __init__(self, tot_len, protocol, saddr, daddr):
        self.ver_len = 0x45  # IP 버전 4와 헤더 길이 5 (5 * 4 = 20바이트)를 나타냅니다. (0x45는 16진수)
        self.tos = 0  # 서비스 유형(Type of Service), 통신의 품질을 나타내며 기본값은 0입니다.
        self.tot_len = tot_len  # 총 길이, 데이터그램의 전체 크기를 바이트 단위로 나타냅니다.
        self.id = 0  # 식별자, 각각의 IP 패킷을 구분하기 위한 값으로, 기본값은 0입니다.
        self.frag_off = 0  # 단편화 오프셋, IP 단편화에서 사용되며 기본값은 0입니다.
        self.ttl = 127  # 패킷 생존 시간(Time To Live), 패킷이 네트워크 상에서 생존할 수 있는 시간을 나타냅니다. 기본값은 127입니다.
        self.protocol = protocol  # 프로토콜, TCP는 6, UDP는 17과 같이 숫자로 표현됩니다.
        self.check = 0  # 헤더 체크섬, 초기값은 0이며 나중에 계산됩니다.
        self.saddr = socket.inet_aton(saddr)  # 출발지 IP 주소, 문자열 형태의 IP 주소를 네트워크 바이트 순서의 4바이트 바이너리 형태로 변환합니다.
        self.daddr = socket.inet_aton(daddr)  # 목적지 IP 주소, 마찬가지로 변환됩니다.

    def pack_Iphdr(self):
        packed = b''  # 빈 바이트 문자열로 시작합니다.
        # struct 패키지의 pack 함수를 사용하여 IP 헤더 필드를 네트워크 바이트 순서(빅 엔디언)의 바이트 문자열로 패킹합니다.
        packed += struct.pack('!BBH', self.ver_len, self.tos, self.tot_len)  # 버전, 서비스 유형, 총 길이
        packed += struct.pack('!HH', self.id, self.frag_off)  # 식별자, 단편화 오프셋
        packed += struct.pack('!BBH', self.ttl, self.protocol, self.check)  # TTL, 프로토콜, 체크섬
        packed += struct.pack('!4s', self.saddr)  # 출발지 주소
        packed += struct.pack('!4s', self.daddr)  # 목적지 주소
        return packed  # 패킹된 바이트 문자열을 반환합니다.
        
# 테스트를 위한 Iphdr 인스턴스를 생성합니다. 여기서는 TCP 프로토콜(6)을 사용합니다.
ip = Iphdr(1000, 6, '10.0.0.1', '11.0.0.1')
packed_iphdr = ip.pack_Iphdr()  # pack_Iphdr 메서드를 호출하여 IP 헤더를 패킹합니다.
print(binascii.b2a_hex(packed_iphdr))  # 패킹된 바이트 문자열을 16진수 형태로 출력합니다.
