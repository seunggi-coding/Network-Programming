import socket

def main():
    host = 'localhost'
    port = 5000
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    message = 'Hello, server! I am 20191516'
    client_socket.sendall(message.encode())
    
    response = client_socket.recv(1024).decode()
    
    print('Received from server: ' + response)
    
    client_socket.close()

if __name__ == "__main__":
    main()