import socket

# 포트 번호와 버퍼 사이즈 설정
port = 2500
BUFFSIZE = 1024

# UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 무한 루프를 돌면서 사용자 입력을 기다림
while True:
    # 사용자로부터 메시지 입력받음
    msg = input('Enter a message: ')
    # 입력받은 메시지가 'q'이면 루프 종료
    if msg == 'q':
        break
    # 입력받은 메시지를 인코딩하여 지정된 주소('localhost', port)로 UDP 패킷을 보냄
    sock.sendto(msg.encode(), ('localhost', port))
    # 서버로부터 응답(에코)을 기다림. 데이터와 서버 주소를 받음
    data, addr = sock.recvfrom(BUFFSIZE)
    # 받은 데이터를 디코딩하여 출력
    print('received:', data.decode())
    
# 소켓을 닫음. 더 이상의 통신이 필요 없음을 나타냄
sock.close()
