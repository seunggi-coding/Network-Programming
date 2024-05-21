from socket import *
import threading

# 서버가 사용할 포트 번호와 버퍼 크기를 정의합니다.
port = 2500
BUFSIZE = 1024

def echoTask(sock):
    # 클라이언트로부터 데이터를 수신하고 다시 전송하는 함수입니다.
    while True:
        data = sock.recv(BUFSIZE)  # 클라이언트로부터 데이터를 수신합니다.
        if not data:
            break  # 수신된 데이터가 없으면 루프를 종료합니다.
        print('Received message:', data.decode())  # 수신된 메시지를 출력합니다.
        sock.send(data)  # 수신된 데이터를 클라이언트로 다시 보냅니다.
    sock.close()  # 소켓을 닫습니다.

# 소켓을 생성하고 설정합니다.
sock = socket(AF_INET, SOCK_STREAM)  # TCP 소켓을 생성합니다.
sock.bind(('', port))  # 지정된 포트로 소켓을 바인딩합니다.
sock.listen(5)  # 최대 5개의 연결을 대기합니다.

while True:
    # 클라이언트의 연결을 수락합니다.
    conn, (remotehost, remoteport) = sock.accept()
    print('connected by', remotehost, remoteport)  # 연결된 클라이언트의 정보를 출력합니다.
    # 새로운 스레드를 생성하여 클라이언트와의 통신을 처리합니다.
    th = threading.Thread(target=echoTask, args=(conn,))
    th.start()  # 스레드를 시작합니다.
