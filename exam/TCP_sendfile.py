import socket
import os

server_address = ('localhost', 12345)
file_path = 'path/to/your/file.txt'  # 전송하고자 하는 파일의 경로

# 서버 소켓 생성 및 바인드
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

print("Waiting for connection...")
connection, client_address = server_socket.accept()

try:
    print(f"Connection from {client_address}")

    # 파일 크기 및 이름 전송
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    connection.send(f"{file_name}:{file_size}".encode())

    # 파일 데이터 전송
    with open(file_path, 'rb') as file:
        connection.sendfile(file)

    print("File has been sent successfully.")

finally:
    connection.close()
    server_socket.close()
