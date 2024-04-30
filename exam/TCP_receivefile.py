import socket
import os

server_address = ('localhost', 12345)
save_directory = 'path/to/save/directory'  # 파일을 저장할 디렉토리 경로

# 클라이언트 소켓 생성 및 서버에 연결
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

# 서버로부터 파일 이름과 크기 수신
file_info = client_socket.recv(1024).decode()
file_name, file_size = file_info.split(':')
file_size = int(file_size)

# 파일 저장 경로 설정 및 파일 수신
save_path = os.path.join(save_directory, file_name)
with open(save_path, 'wb') as file:
    remaining = file_size
    while remaining:
        chunk_size = 4096 if remaining >= 4096 else remaining
        chunk = client_socket.recv(chunk_size)
        if not chunk: break
        file.write(chunk)
        remaining -= len(chunk)

print(f"File has been received and saved to {save_path}.")

client_socket.close()
