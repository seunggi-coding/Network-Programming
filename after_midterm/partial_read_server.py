from socket import *

server = create_server(('', 9999))
conn, addr = server.accept()

conn.send(b'This is IoT world!!')
conn.close()