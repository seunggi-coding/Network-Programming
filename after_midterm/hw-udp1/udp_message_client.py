import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter the message('send mboxId message' 또는 'receive mboxId'):")
    client_socket.sendto(message.encode(), ('localhost', 2530))
    
    if message == 'quit':
        break
    
    response, addr = client_socket.recvfrom(1024)
    print(response.decode())

client_socket.close()
