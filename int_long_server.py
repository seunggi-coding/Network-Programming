# 정수 송신
# 방법 1 (문자열로 변경한 후, 송수신한 후 다시 정수로 변경)
import socket
import struct

# 서버의 주소와 포트 설정
server_address = 'localhost'
server_port = 12345

# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 주소 재사용 설정
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 주소와 포트 바인딩
server_socket.bind((server_address, server_port))

# 연결 대기
server_socket.listen(1)
print("클라이언트의 연결을 기다리고 있습니다...")

# 클라이언트 연결 수락
client_socket, addr = server_socket.accept()
print(f"{addr}로부터 연결됨")

# 클라이언트로부터 정수 수신
data = client_socket.recv(4)  # 4 바이트 데이터 수신
received_int = struct.unpack('i', data)[0]  # 받은 바이트 데이터를 정수로 변환
print(f"클라이언트로부터 받은 정수: {received_int}")

# 수신된 정수에 1을 더해서 클라이언트로 전송
new_int = received_int + 1
client_socket.send(struct.pack('i', new_int))

# 연결 종료
client_socket.close()
server_socket.close()


# 방법 2 (int <-> bytes 직접 변환 / int.to_bytes(), int.from_bytes())
import socket

# 서버의 주소와 포트 설정
server_address = 'localhost'
server_port = 12345

# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 주소 재사용 옵션 설정
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 소켓을 주소와 포트에 바인딩
server_socket.bind((server_address, server_port))

# 연결 대기 상태로 전환
server_socket.listen(1)
print("클라이언트의 연결을 기다리고 있습니다...")

# 클라이언트의 연결 요청 수락
client_socket, addr = server_socket.accept()
print(f"{addr} 주소에서 연결되었습니다.")

# 클라이언트로부터 데이터 수신 (from_bytes())
data = client_socket.recv(4)  # 4 바이트 데이터 수신
received_int = int.from_bytes(data, byteorder='big')  # 바이트를 정수로 변환
print(f"클라이언트로부터 수신된 정수: {received_int}")

# 클라이언트에게 정수 송신
new_int = received_int + 1
client_socket.send(new_int.to_bytes(4, byteorder='big'))

# 연결 종료
client_socket.close()
server_socket.close()
