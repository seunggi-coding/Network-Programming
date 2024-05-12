from socket import *
import os

BUF_SIZE = 1024  # 버퍼 크기 설정
LENGTH = 4  # 파일 크기 정보를 전송할 때 사용할 바이트 수

sock = socket(AF_INET, SOCK_STREAM)  # IPv4, TCP 소켓 생성
sock.bind(('', 7777))  # 모든 인터페이스의 7777 포트에 바인드
sock.listen(10)  # 최대 10개의 클라이언트 연결 대기
print('File server is running...')

while True:
    conn, addr = sock.accept()  # 클라이언트 연결 수락
    msg = conn.recv(BUF_SIZE)  # 클라이언트로부터 'Hello' 메시지 수신
    if not msg:  # 메시지가 없는 경우 연결 종료
        conn.close()
        continue
    elif msg != b'Hello':  # 'Hello'가 아닌 다른 메시지 수신 시 로그 출력 후 연결 종료
        print('client:', addr, msg.decode())
        conn.close()
        continue
    else:  # 올바른 메시지('Hello') 수신 시 클라이언트 정보 출력
        print('client:', addr, msg.decode())
        
    # 클라이언트에게 'Filename' 메시지 전송
    conn.send(b'Filename')
    
    # 클라이언트로부터 파일 이름 수신
    msg = conn.recv(BUF_SIZE)
    if not msg:  # 메시지가 없는 경우 연결 종료
        conn.close()
        continue
    filename = msg.decode()
    print('client:', addr, filename)  # 수신된 파일 이름 출력
    
    try:
        filesize = os.path.getsize(filename)  # 파일 크기 확인
    except:
        conn.send(b'Nofile')  # 파일이 없는 경우 'Nofile' 메시지 전송
        conn.close()
        continue
    else:  # 파일이 있는 경우
        # 파일 크기를 4바이트로 변환하여 전송
        fs_binary = filesize.to_bytes(LENGTH, 'big')
        conn.send(fs_binary)
        
    f = open(filename, 'rb')  # 파일을 바이너리 읽기 모드로 열기
    data = f.read()  # 파일의 모든 내용을 읽기
    conn.sendall(data)  # 파일의 모든 데이터를 클라이언트에게 전송
    
    msg = conn.recv(BUF_SIZE)  # 클라이언트로부터 'Bye' 메시지 수신
    if not msg:
        pass
    else:  # 'Bye' 메시지 수신 시 출력
        print('client:', addr, msg.decode())
    f.close()  # 파일 닫기
    conn.close()  # 클라이언트와의 연결 종료
