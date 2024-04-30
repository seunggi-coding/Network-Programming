import socket

# 소켓 객체 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 서버의 주소와 포트에 연결
client_socket.connect(('localhost', 12345))

try:
    # 서버에게 3번 데이터 송신
    for i in range(1, 4):
        message = f"클라이언트 메시지 {i}"
        client_socket.send(message.encode())

    # 서버로부터 4번 데이터 수신
    for _ in range(4):
        data = client_socket.recv(1024)
        print(f"서버로부터 받은 데이터: {data.decode()}")
finally:
    client_socket.close()
