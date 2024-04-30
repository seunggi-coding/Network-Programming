import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 2530))

client_socket.send("Seung Gi Moon".encode())

data = client_socket.recv(1024)
received_int = int.from_bytes(data, 'big')

print(f"Received and converted Student ID: {received_int}")

client_socket.close()
