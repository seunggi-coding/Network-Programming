import socket

# 소켓 객체 생성: AF_INET은 IPv4 주소 체계를, SOCK_STREAM은 TCP 연결 지향 프로토콜을 사용함을 의미합니다.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 주소 설정: 'localhost'는 현재 컴퓨터를 의미하며, 포트 번호는 9000입니다.
addr = ('localhost', 9000)

# 서버에 연결 요청: 설정한 주소(addr)의 서버에 연결을 시도합니다.
sock.connect(addr)

# 서버로부터 메시지 수신: recv 함수를 사용하여 서버로부터 메시지를 수신합니다.
# 인자 1024는 한 번에 수신할 수 있는 최대 바이트 수를 의미합니다.
msg = sock.recv(1024)

# 수신된 메시지 출력: 수신된 메시지는 바이트 형태이므로, decode 함수를 사용하여 문자열로 변환한 후 출력합니다.
print(msg.decode())

# 소켓 연결 종료: 사용이 끝난 소켓을 닫습니다.
sock.close()
