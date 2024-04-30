import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 2530))
server_socket.listen()

print("Server is listening...")

client_socket, addr = server_socket.accept()
print(f"Connection from: {addr}")

data = client_socket.recv(1024)
print(f"Student Name: {data.decode()}")

number_to_send = 20191516
client_socket.send(number_to_send.to_bytes(4, 'big'))


client_socket.close()
server_socket.close()
