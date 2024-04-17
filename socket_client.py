# 클라이언트 측 메소드

import socket
import array

# 서버의 주소와 포트
server_address = 'localhost'
server_port = 12345

# 클라이언트 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결 요청
client_socket.connect((server_address, server_port))
print("서버에 연결되었습니다.")

# 사용자 입력 받기
user_input = input("서버로 전송할 메시지를 입력하세요: ")
# 입력받은 문자열을 바이트로 변환하여 서버로 송신 (encode)
client_socket.send(user_input.encode('utf-8'))

# 서버로 데이터 송신 (send)
client_socket.send(b"Hello, server! (send)")

# 서버로 데이터 송신 (sendall)
client_socket.sendall(b"Hello, server again! (sendall)")

# 서버로부터 데이터 수신 (recv)
data = client_socket.recv(1024)
print("수신된 데이터 (recv):", data.decode())

# recv_into() 사용을 위한 버퍼 생성
buffer = array.array('b', [0]*1024)  # 1024 바이트 크기의 버퍼
# 서버로부터 데이터 수신하여 버퍼에 저장 (recv_into)
recv_size = client_socket.recv_into(buffer)
print("수신된 데이터 (recv_into):", buffer[:recv_size].tobytes().decode())

# 연결 종료
client_socket.close()
print("서버와의 연결이 종료되었습니다.")
