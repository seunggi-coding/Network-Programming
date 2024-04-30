from socket import *

port = 2500
BUFFSIZE = 1024

sock = create_server(('', port), family=AF_INET, backlog=1)
conn, (remotehost, remoteport) = sock.accept()
print('connected by', remotehost, remoteport)

while True:
    data = conn.recv(BUFFSIZE)
    if not data:
        break
    print('Received message:', data.decode())
    conn.send(data)
    
conn.close()