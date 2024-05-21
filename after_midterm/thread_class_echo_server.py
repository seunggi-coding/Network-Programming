from socket import *
import threading

# 서버가 사용할 포트 번호 및 버퍼 크기를 정의합니다.
port = 2500
BUFSIZE = 1024

# 클라이언트와의 통신을 처리할 스레드 클래스 정의
class ClientThread(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)  # 부모 클래스의 초기화 메서드 호출
        self.sock = sock  # 전달받은 소켓 객체를 인스턴스 변수로 저장
    
    def run(self):
        # 클라이언트로부터 데이터를 받고 에코하는 메서드
        while True:
            data = self.sock.recv(BUFSIZE)  # 클라이언트로부터 데이터를 수신
            if not data:
                break  # 데이터가 없으면 루프 종료
            print('Received message:', data.decode())  # 수신한 메시지를 출력
            self.sock.send(data)  # 수신한 데이터를 클라이언트로 다시 전송
        self.sock.close()  # 소켓을 닫음

# 서버 소켓 생성 및 설정
sock = socket(AF_INET, SOCK_STREAM)  # TCP 소켓 생성
sock.bind(('', port))  # 소켓을 지정된 포트에 바인딩
sock.listen(5)  # 최대 5개의 연결을 대기

while True:
    # 클라이언트 연결 수락
    conn, (remotehost, remoteport) = sock.accept()
    print('connected by', remotehost, remoteport)  # 연결된 클라이언트 정보 출력
    # 클라이언트와 통신을 처리할 새로운 스레드 생성 및 시작
    th = ClientThread(conn)
    th.start()
