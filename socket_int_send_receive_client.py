import socket

# 클라이언트 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))  # 서버에 연결

# 송신할 정수
number_to_send = 12345
# 정수를 바이트로 변환하여 송신
client_socket.send(number_to_send.to_bytes(4, 'big'))

print(f"{number_to_send} 정수를 서버로 송신하였습니다.")

# 연결 종료
client_socket.close()
