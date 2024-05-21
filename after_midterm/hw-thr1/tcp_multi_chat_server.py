import socket
import threading

clients = []

def client_handler(client_sock, addr):
    print(f'New client {addr} connected.')
    clients.append(client_sock)
    
    while True:
        try:
            data = client_sock.recv(1024)
            if not data:
                break
            message = data.decode()
            if 'quit' in message:
                print(f'Client {addr} has requested to disconnect.')
                break
            
            print(f'{addr}: {message}')
            for client in clients:
                if client != client_sock:
                    client.send(data)
        except ConnectionResetError:
            break

    if client_sock in clients:
        clients.remove(client_sock)
    client_sock.close()
    print(f'Client {addr} disconnected.')

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('', 2500))
server_sock.listen(3)
print('Server 시작..')

while True:
    client_sock, addr = server_sock.accept()
    th = threading.Thread(target=client_handler, args=(client_sock, addr))
    th.start()
