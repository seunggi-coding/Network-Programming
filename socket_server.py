# 서버 측 메소드

import socket

# 서버의 주소와 포트 설정
server_address = 'localhost'
server_port = 12345

# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 주소 재사용 옵션 설정
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 소켓을 주소와 포트에 바인딩
server_socket.bind((server_address, server_port))

# 연결 대기 상태로 전환
server_socket.listen()
print("클라이언트의 연결을 기다리고 있습니다...")

# 클라이언트의 연결 요청 수락
client_socket, addr = server_socket.accept()
print(f"{addr} 주소에서 연결되었습니다.")

# 첫 번째 클라이언트로부터 데이터 수신 (recv) - 사용자 입력
data = client_socket.recv(1024)
print(f"클라이언트로부터 수신된 첫 번째 메시지 (recv): {data.decode()}")

# 두 번째 클라이언트로부터 데이터 수신 (recv) - "Hello, server! (send)"
data = client_socket.recv(1024)
print(f"클라이언트로부터 수신된 두 번째 메시지 (recv): {data.decode()}")

# 세 번째 클라이언트로부터 데이터 수신 (recv) - "Hello, server again! (sendall)"
data = client_socket.recv(1024)
print(f"클라이언트로부터 수신된 세 번째 메시지 (recv): {data.decode()}")

# 클라이언트에게 데이터 송신 (send)
client_socket.send(b"Hello, client! (send)")

# 클라이언트에게 데이터 송신 (sendall)
client_socket.sendall(b"Goodbye, client! (sendall)")

# 연결 종료
client_socket.close()
server_socket.close()
print("클라이언트와의 연결이 종료되었습니다.")
