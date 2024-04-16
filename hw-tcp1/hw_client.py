import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

#본인의 이름을 문자열로 전송
myName = 'Seung Gi Moon'  # 이름
sock.send(myName.encode())

#본인의 학번을 수신 후 출력
myId_bytes = sock.recv(1024)
myId = int.from_bytes(myId_bytes, 'big')
print('학번:', myId)

sock.close()