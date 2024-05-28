# 클라이언트 코드는 echo_client.py를 사용하면 된다. 굳이 동시성을 고려할 이유가 없기 때문.
import socket, select

socks = []  # 서버와 클라이언트 소켓을 관리할 리스트
BUFFER = 1024  # 버퍼 크기 설정
PORT = 2500  # 서버가 사용할 포트 번호 설정

# 서버 소켓 생성
s_sock = socket.socket()
# 서버 소켓을 지정된 포트에 바인딩
s_sock.bind(('', PORT))
# 서버 소켓을 클라이언트의 연결을 대기하도록 설정
s_sock.listen(5)

# 서버 소켓을 소켓 리스트에 추가
socks.append(s_sock)
print(str(PORT) + '에서 접속 대기 중')

# 무한 루프 실행
while True:
    # select를 사용하여 읽기 가능한 소켓들을 검사
    r_sock, w_sock, e_sock = select.select(socks, [], [])
    
    # 읽기 가능한 소켓들을 순회
    for s in r_sock:
        # 서버 소켓이 읽기 가능하면 (즉, 새로운 연결이 들어옴)
        if s == s_sock:
            # 클라이언트 소켓과 주소를 받아옴
            c_sock, addr = s_sock.accept()
            # 새로운 클라이언트 소켓을 소켓 리스트에 추가
            socks.append(c_sock)
            # 클라이언트 연결 정보를 출력
            print('Client ({}) connected'.format(addr))
        else:
            # 클라이언트 소켓이 읽기 가능하면 (즉, 데이터가 수신됨)
            data = s.recv(BUFFER)
            # 수신된 데이터가 없으면 (즉, 클라이언트가 연결을 닫음)
            if not data:
                # 소켓을 닫고 소켓 리스트에서 제거
                s.close()
                socks.remove(s)
                continue
            # 수신된 데이터를 출력
            print('Received:', data.decode())
            # 수신된 데이터를 다시 클라이언트에게 에코
            s.send(data)
