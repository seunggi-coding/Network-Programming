import socket

# socket.socket 함수를 사용하여 소켓 객체를 생성합니다.
# AF_INET은 IPv4 인터넷 프로토콜을, SOCK_STREAM은 TCP 연결 방식을 의미합니다.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind 함수를 사용하여 생성한 소켓을 주소와 포트에 바인딩합니다.
# 여기서 ''는 모든 인터페이스에서 연결을 수락하겠다는 의미이고, 9000은 포트 번호입니다.
s.bind(('', 9000))

# listen 함수를 사용하여 소켓을 리스닝(수신 대기) 상태로 만듭니다.
# 인자는 동시에 연결을 수락할 수 있는 최대 클라이언트 수를 의미합니다.
s.listen(2)

# 무한 루프를 사용하여 클라이언트의 연결을 계속해서 기다립니다.
while True:
    print("연결을 대기중..")
    # accept 함수는 클라이언트의 연결 요청을 수락합니다.
    # 이 함수는 연결이 수립되면, 연결된 클라이언트와 그 주소를 나타내는 새로운 소켓 객체와 주소를 반환합니다.
    client, addr = s.accept()
    # 클라이언트의 주소 정보를 출력합니다.
    print('Connection from ', addr)
    
    # 클라이언트에게 메시지를 보냅니다. 여기서 addr[0]은 클라이언트의 IP 주소를 의미하며,
    # 이를 encode 함수를 사용하여 바이트로 변환한 후 'Hello ' 메시지와 결합하여 전송합니다.
    client.send(b'Hello ' + addr[0].encode())
    
    # 데이터 전송이 끝난 후 클라이언트와의 연결을 종료합니다.
    client.close()
