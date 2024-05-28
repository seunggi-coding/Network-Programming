# 클라이언트 코드는 echo_client.py를 사용하면 된다. 굳이 동시성을 고려할 이유가 없기 때문.
import socket
import selectors  # selectors 모듈을 사용하여 비동기 입출력 처리

sel = selectors.DefaultSelector()  # 기본 Selector 객체 생성

# 새로운 클라이언트 연결을 처리하는 함수
def accept(sock, mask):
    conn, addr = sock.accept()  # 클라이언트 연결 수락
    print('Connected by', addr)  # 클라이언트 주소 출력
    sel.register(conn, selectors.EVENT_READ, read)  # 클라이언트 소켓을 읽기 이벤트에 등록

# 클라이언트로부터 데이터를 읽는 함수
def read(conn, mask):
    data = conn.recv(1024)  # 클라이언트로부터 데이터 수신
    if not data:
        sel.unregister(conn)  # 데이터가 없으면(연결 종료) Selector에서 해당 소켓 등록 해제
        conn.close()  # 소켓 닫기
    else:
        print('Received:', data.decode())  # 수신된 데이터 출력
        conn.send(data)  # 받은 데이터를 그대로 클라이언트에게 전송(에코)

# 서버 소켓 생성
sock = socket.socket()
# 서버 소켓을 지정된 포트에 바인딩
sock.bind(('', 2500))  # 빈 문자열을 주소로 사용하여 모든 인터페이스의 2500 포트에서 접속 대기
# 서버 소켓을 클라이언트의 연결을 대기하도록 설정
sock.listen(5)  # 동시에 5개의 클라이언트까지 연결 대기

sel.register(sock, selectors.EVENT_READ, accept)  # 서버 소켓을 읽기 이벤트에 등록

# 무한 루프 실행
while True:
    events = sel.select()  # 이벤트가 발생할 때까지 대기, 발생하면 해당 이벤트 목록 반환
    for key, mask in events:
        callback = key.data  # 등록된 콜백 함수
        callback(key.fileobj, mask)  # 콜백 함수 호출, 소켓과 마스크를 인자로 전달
