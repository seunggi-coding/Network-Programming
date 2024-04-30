import socket
import select

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# 서버로부터 메시지가 있는지 확인합니다.
ready = select.select([client_socket], [], [], 5)  # 5초 동안 대기
if ready[0]:
    data = client_socket.recv(1024)
    print(f"서버로부터 수신된 메시지: {data.decode()}")

# 서버로부터 메시지가 없으면, 클라이언트는 자신의 메시지를 송신합니다.
else:
    message = "클라이언트에서 서버로 메시지를 보냅니다."
    client_socket.send(message.encode())
    data = client_socket.recv(1024)
    print(f"서버로부터 응답 받은 메시지: {data.decode()}")

client_socket.close()
