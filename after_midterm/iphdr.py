import socket

class Iphdr:
    # IP 헤더 클래스 초기화
    def __init__(self, tot_len, protocol, saddr, daddr):
        self.ver_len = 0x45  # IP 버전과 헤더 길이 (IPv4, 5 * 4 = 20바이트)
        self.tos = 0  # 서비스 유형(Type of Service), 기본값 0
        self.tot_len = tot_len  # 전체 패킷 길이
        self.id = 0  # 식별자, 기본값 0
        self.frag_off = 0  # 단편화 오프셋, 기본값 0
        self.ttl = 127  # 패킷 생존 시간(Time To Live), 기본값 127
        self.protocol = protocol  # 프로토콜 (TCP는 6, UDP는 17)
        self.check = 0  # 헤더 체크섬, 초기에는 0
        self.saddr = socket.inet_aton(saddr)  # 출발지 주소를 바이너리 형태로 변환
        self.daddr = socket.inet_aton(daddr)  # 목적지 주소를 바이너리 형태로 변환

# 테스트를 위한 Iphdr 인스턴스 생성, 여기서는 TCP 프로토콜(6)을 사용합니다.
test = Iphdr(1000, 6, '10.0.0.1', '11.0.0.1')

# 소켓 생성, 여기서는 UDP 소켓을 사용합니다.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 생성한 IP 헤더를 바이트 형태로 변환하여 'localhost'의 2500 포트로 보냅니다.
# 이 코드는 실제로 IP 헤더를 올바르게 처리하지 않습니다. bytes(test)는 클래스 인스턴스를 바이트로 직접 변환할 수 없으므로 오류를 발생시킵니다.
# 실제 네트워크 프로그래밍에서는 struct 모듈을 사용하여 필드를 적절한 형태로 패킹해야 합니다.
sock.sendto(bytes(test), ('localhost', 2500))
