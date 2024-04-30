import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("서버가 클라이언트의 연결을 기다립니다...")

client_socket, addr = server_socket.accept()
print(f"{addr}에서 연결되었습니다.")

# 서버가 먼저 메시지를 보낼 수 있습니다. 주석 처리하여 선택적으로 활성화할 수 있습니다.
# client_socket.send("서버에서 클라이언트로 먼저 메시지를 보냅니다.".encode())

while True:
    # 클라이언트로부터 메시지를 기다립니다.
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"수신된 메시지: {data.decode()}")

    # 클라이언트에 메시지를 응답합니다.
    message = "서버에서의 응답 메시지입니다."
    client_socket.send(message.encode())

client_socket.close()
server_socket.close()
