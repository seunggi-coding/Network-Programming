from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)

print("서버가 준비되었습니다.")

while True:
    c, addr = s.accept()
    
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')[0]
    method, path, http_version = req.split(' ')
    
    if path == '/index.html':
        f = open('index.html', 'r', encoding='utf-8')
        content = f.read()
        c.send('HTTP/1.1 200 OK\r\n'.encode('utf-8'))
        c.send('Content-Type: text/html\r\n'.encode('utf-8'))
        c.send('\r\n'.encode('utf-8'))
        c.send(content.encode('utf-8'))
        f.close()
    
    elif path == '/iot.png':
        f = open('iot.png', 'rb')
        content = f.read()
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        c.send('Content-Type: image/png\r\n'.encode())
        c.send('\r\n'.encode())
        c.send(content)
        f.close()

    elif path == '/favicon.ico':
        f = open('favicon.ico', 'rb')
        content = f.read()
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        c.send('Content-Type: image/x-icon\r\n'.encode())
        c.send('\r\n'.encode())
        c.send(content)
        f.close()
    
    else:
        c.send('HTTP/1.1 404 Not Found\r\n'.encode('utf-8'))
        c.send('\r\n'.encode('utf-8'))
        c.send('<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'.encode('utf-8'))
        c.send('<BODY>Not Found</BODY></HTML>'.encode('utf-8'))
    
    c.close()
