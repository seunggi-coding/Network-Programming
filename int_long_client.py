# 정수 송수신
# 방법 1 (문자열로 변경한 후, 송수신한 후 다시 정수로 변경)

import socket
import struct

# 서버의 주소와 포트
server_address = 'localhost'
server_port = 12345

# 클라이언트 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결
client_socket.connect((server_address, server_port))
print("서버에 연결되었습니다.")

# 전송할 정수
num_to_send = 15
# 정수를 바이트 객체로 변환하여 전송
client_socket.send(struct.pack('i', num_to_send))

# 서버로부터 정수 수신
data = client_socket.recv(4)  # 4 바이트 데이터 수신
received_int = struct.unpack('i', data)[0]  # 받은 바이트 데이터를 정수로 변환
print(f"서버로부터 받은 정수: {received_int}")

# 연결 종료
client_socket.close()


# 방법 2 (int <-> bytes 직접 변환 / int.to_bytes(), int.from_bytes())
import socket

# 서버의 주소와 포트
server_address = 'localhost'
server_port = 12345

# 클라이언트 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결 요청
client_socket.connect((server_address, server_port))
print("서버에 연결되었습니다.")

# 송신할 정수
num_to_send = 15
# 정수를 바이트로 변환하여 송신 (to_bytes())
client_socket.send(num_to_send.to_bytes(4, byteorder='big'))

# 서버로부터 데이터 수신
data = client_socket.recv(4)  # 4 바이트 데이터 수신
received_int = int.from_bytes(data, byteorder='big')  # 바이트를 정수로 변환
print(f"서버로부터 수신된 정수: {received_int}")

# 연결 종료
client_socket.close()
