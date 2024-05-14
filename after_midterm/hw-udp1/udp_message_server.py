import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 2530))

messages = {}

while True:
    data, addr = server_socket.recvfrom(1024)
    command = data.decode().split(' ', 2)
    
    if command[0] == 'send':
        mboxID = command[1]
        message = command[2]
        if mboxID not in messages:
            messages[mboxID] = []
        messages[mboxID].append(message)
        server_socket.sendto(b'OK', addr)
    
    elif command[0] == 'receive':
        mboxID = command[1]
        if mboxID in messages and messages[mboxID]:
            server_socket.sendto(messages[mboxID].pop(0).encode(), addr)
        else:
            server_socket.sendto(b'No messages', addr)
    
    elif command[0] == 'quit':
        break

server_socket.close()
