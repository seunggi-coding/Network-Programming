import socket
import sys
import struct

class DnsClient:
    def __init__(self, domainName):
        # 주어진 도메인 이름으로 DNS 클라이언트 초기화
        self.domainName = domainName
        
        # DNS 쿼리 파라미터
        self.TransactionId = 1       # DNS 쿼리를 위한 고유 식별자
        self.Flags = 0x0100          # 표준 쿼리이며 재귀를 원함을 나타냄
        self.Questions = 1           # 질문 개수
        self.AnserRRs = 0            # 응답 리소스 레코드의 수
        self.AuthorityRRs = 0        # 권한 리소스 레코드의 수
        self.AdditionalRRs = 0       # 추가 리소스 레코드의 수
    
    def response(self, packet):
        # 응답 패킷 분석
        
        # 패킷의 처음 12바이트는 DNS 헤더
        dnsHeader = packet[:12]
        
        # 헤더 이후의 DNS 데이터는 첫 번째 널 바이트에서 분리됨
        dnsData = packet[12:].split(b'\x00', 1)
        
        # 응답 리소스 레코드(RR) 섹션 추출
        # 질문 섹션 이후에 시작하며 길이는 21바이트
        ansRR = packet[12 + len(dnsData[0]) + 5:12 + len(dnsData[0]) + 21]
        
        # 응답 RR 섹션을 분석
        rr_unpack = struct.unpack('!2sHHIH4s', ansRR)
        
        # 응답 RR에서 IP 주소를 추출하고 사람이 읽을 수 있는 형식으로 변환
        ip_addr = socket.inet_ntoa(rr_unpack[5])
        
        # 도메인 이름과 해석된 IP 주소 출력
        print(self.domainName, ip_addr)
        
    def query(self):
        # DNS 쿼리 구성
        
        # DNS 헤더 생성
        query = struct.pack('!HH', self.TransactionId, self.Flags)
        query += struct.pack('!HH', self.Questions, self.AnserRRs)
        query += struct.pack('!HH', self.AuthorityRRs, self.AdditionalRRs)
        
        # 도메인 이름을 그 구성 요소로 분할
        part = self.domainName.split('.')
        
        # 도메인 이름의 각 부분을 인코딩하고 쿼리에 추가
        for i in range(len(part)):
            query = query + struct.pack('!B', len(part[i]))
            query = query + part[i].encode()
        
        # 도메인 이름의 끝을 나타내기 위해 널 바이트 추가
        query = query + b'\x00'
        
        # 쿼리 유형(A 레코드)과 쿼리 클래스(IN - 인터넷) 지정
        query_type = 1
        query_class = 1
        query = query + struct.pack('!HH', query_type, query_class)
        
        # UDP 소켓 생성
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # DNS 서버 주소(예: 구글의 공개 DNS 서버)
        addr = ('220.69.193.130', 53)
        
        # 쿼리를 서버로 전송
        sock.sendto(query, addr)
        
        # 서버로부터 응답 패킷 수신
        packet, address = sock.recvfrom(65535)
        
        # 응답 패킷 처리
        self.response(packet)

# 스크립트의 시작점
if __name__ == '__main__':
    # 커맨드 라인 인자로 도메인 이름이 제공되었는지 확인
    if len(sys.argv) > 1:
        # 제공된 도메인 이름으로 DnsClient 인스턴스 생성
        client = DnsClient(sys.argv[1])
        
        # DNS 쿼리 수행
        client.query()
