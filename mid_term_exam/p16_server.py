import socket
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    print('Sersver is listening on port 5000')

    client_socket, addr = server_socket.accept()
    print(f"Connection from: ({addr})")

    data = client_socket.recv(1024)
    data_list = data.decode().split(" ")
        
    print(f'Received from client: {data.decode()}')

    client_socket.send(f'Hi, stranger! You are {data_list[-1]}'.encode())

    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()