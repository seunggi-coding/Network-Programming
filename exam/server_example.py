import socket

# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind(): 소켓에 주소와 포트를 할당합니다.
server_socket.bind(('localhost', 12345))

# listen(): 서버가 클라이언트의 연결을 수신하기 시작합니다.
server_socket.listen()

print("서버가 연결을 기다리고 있습니다.")

# accept(): 클라이언트의 연결 요청을 수락합니다.
client_socket, addr = server_socket.accept()

print(f"{addr}에서 연결되었습니다.")

# recv(): 클라이언트로부터 데이터를 수신합니다.
data = client_socket.recv(1024)
print(f"수신된 데이터: {data.decode()}")

# send(): 클라이언트로 데이터를 송신합니다.
client_socket.send("안녕 클라이언트!".encode())

# close(): 소켓 연결을 종료합니다.
client_socket.close()
server_socket.close()
