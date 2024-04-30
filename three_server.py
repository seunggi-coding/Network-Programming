import socket

# 소켓 객체 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 로컬 호스트와 포트 12345에 바인드
server_socket.bind(('localhost', 12345))
# 클라이언트의 연결을 기다림
server_socket.listen(1)

print("서버가 클라이언트의 연결을 기다리고 있습니다...")
client_socket, addr = server_socket.accept()
print(f"{addr}에서 연결되었습니다.")

try:
    # 클라이언트로부터 3번 데이터 수신
    for _ in range(3):
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"클라이언트로부터 받은 데이터: {data.decode()}")

    # 클라이언트에게 4번 데이터 송신
    for i in range(1, 5):
        message = f"메시지 {i}"
        client_socket.send(message.encode())
finally:
    client_socket.close()
    server_socket.close()
    print("서버 연결을 종료합니다.")
