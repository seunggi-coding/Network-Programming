import socket

# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))  # 주소와 포트 바인딩
server_socket.listen()  # 클라이언트의 연결 대기

print("서버 시작. 클라이언트의 연결을 기다립니다...")

# 연결 수락
client_socket, addr = server_socket.accept()
print(f"{addr} 클라이언트가 연결되었습니다.")

# 데이터 수신
data = client_socket.recv(1024)
received_int = int.from_bytes(data, 'big')  # 바이트를 정수로 변환
print(f"수신된 정수: {received_int}")

# 연결 종료
client_socket.close()
server_socket.close()
