from socket import *
import os

def send_file(c, filename, mimeType):
    try:
        with open(filename, 'rb') as f:  # 바이너리 모드로 파일을 엽니다.
            data = f.read()
            # HTTP 헤더 전송
            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: ' + mimeType + '\r\n\r\n'
            c.send(header.encode())
            # HTTP 바디 전송
            c.send(data)
    except FileNotFoundError:
        # 해당 파일이 존재하지 않는 경우, 404 메시지 전송
        response = 'HTTP/1.1 404 Not Found\r\n\r\n'
        response += '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
        response += '<BODY>Not Found</BODY></HTML>'
        c.send(response.encode('euc-kr'))

# 소켓 설정
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)

print("The server is ready.")

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    start_line = msg.split('\r\n')[0]  # 요청 라인 추출
    method, path, version = start_line.split()  # 메서드, 경로, 버전 분리
    
    # 파싱한 파일 이름 "/" 제거
    filename = path.lstrip('/')
    
    # MIME 타입 설정
    if filename == 'index.html':
        mimeType = 'text/html; charset=utf-8'
        send_file(c, filename, mimeType)
    elif filename == 'iot.png':
        mimeType = 'image/png'
        send_file(c, filename, mimeType)
    elif filename == 'favicon.ico':
        mimeType = 'image/x-icon'
        send_file(c, filename, mimeType)
    else:
        # 지원하지 않는 자원 요청 시 "Not Found" 메시지 전송
        mimeType = 'text/html; charset=utf-8'
        send_file(c, 'notfound.html', mimeType)
        
    c.close()  # 소켓 닫기
