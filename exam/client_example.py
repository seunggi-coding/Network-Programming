import socket

# 클라이언트 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect(): 서버에 연결을 시도합니다.
client_socket.connect(('localhost', 12345))

# send(): 서버로 데이터를 송신합니다.
client_socket.send("안녕 서버!".encode())

# recv(): 서버로부터 데이터를 수신합니다.
data = client_socket.recv(1024)
print(f"수신된 데이터: {data.decode()}")

# close(): 소켓 연결을 종료합니다.
client_socket.close()
