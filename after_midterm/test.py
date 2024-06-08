import socket
import struct, binascii

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

    def pack_header(self):
        # struct.pack을 사용하여 IP 헤더를 바이트 형태로 패킹
        return struct.pack('!BBHHHBBH4s4s',
                           self.ver_len, self.tos, self.tot_len,
                           self.id, self.frag_off, self.ttl, self.protocol,
                           self.check, self.saddr, self.daddr)

# 테스트를 위한 Iphdr 인스턴스 생성, 여기서는 TCP 프로토콜(6)을 사용합니다.
test = Iphdr(1000, 6, '10.0.0.1', '11.0.0.1')

packed_iphdr = test.pack_header() 
print(binascii.b2a_hex(packed_iphdr))
