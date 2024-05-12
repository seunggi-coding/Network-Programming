import socket

# 포트 번호 설정
port = 2500
# 버퍼 크기 설정 (한 번에 전송받거나 보낼 수 있는 최대 데이터 양)
BUFFSIZE = 1024

# 소켓 생성
# AF_INET은 IPv4 인터넷 프로토콜을 사용함을 의미하며, SOCK_DGRAM은 UDP 프로토콜을 사용함을 의미합니다.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 생성된 소켓에 IP 주소와 포트 번호를 할당합니다. ''는 모든 인터페이스와 바인딩되며, 주어진 포트를 사용합니다.
sock.bind(('', port))

# 무한 반복을 통해 지속적으로 메시지를 수신하고 응답합니다.
while True:
    # 소켓을 통해 데이터와 상대방의 주소 정보를 수신합니다. BUFFSIZE로 지정된 크기만큼 데이터를 받을 수 있습니다.
    msg, addr = sock.recvfrom(BUFFSIZE)
    # 수신된 메시지를 디코딩하여 출력합니다.
    print('received:', msg.decode())
    # 상대방에게 수신된 메시지를 그대로 보냅니다. 에코 서버의 기능을 수행합니다.
    sock.sendto(msg, addr)
