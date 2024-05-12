from socket import *
import sys

BUF_SIZE = 1024  # 버퍼 사이즈 설정
LENGTH = 4  # '파일 크기'를 나타내는데 사용할 바이트 수

s = socket(AF_INET, SOCK_STREAM)  # 소켓 생성
s.connect(('localhost', 7777))  # 서버에 연결

s.send(b'Hello')  # 서버에 'Hello' 메시지를 전송

msg = s.recv(BUF_SIZE)  # 서버로부터 'Filename' 메시지를 기다림
if not msg:
    s.close()
    sys.exit()  # 메시지가 없다면 연결 종료 후 프로그램 종료
elif msg != b'Filename':
    print('server:', msg.decode())  # 예상치 못한 메시지를 받았을 경우 출력
    s.close()
    sys.exit()  # 연결 종료 후 프로그램 종료
else:
    print('server:', msg.decode())  # 'Filename' 메시지를 받았다면 출력
    
filename = input('Enter a filename: ')  # 전송받고 싶은 파일 이름 입력
s.send(filename.encode())  # 입력받은 파일 이름을 서버에 전송

msg = s.recv(BUF_SIZE)  # 서버로부터 파일 크기를 수신
if not msg:
    s.close()
    sys.exit()  # 메시지가 없다면 연결 종료 후 프로그램 종료
elif msg == b'Nofile':
    print('server:', msg.decode())  # 파일이 없다는 메시지를 받았을 경우 출력
    s.close()
    sys.exit()  # 연결 종료 후 프로그램 종료
else:
    rx_size = len(msg)
    data = msg
    while rx_size < LENGTH:  # 파일 크기 정보가 완전히 수신될 때까지 반복
        msg = s.recv(BUF_SIZE)
        if not msg:
            s.close()
            sys.exit()  # 중간에 연결이 끊긴 경우
        data = data + msg
        rx_size += len(msg)
    if rx_size < LENGTH:
        s.close()
        sys.exit()  # 필요한 길이만큼 데이터를 받지 못한 경우

    filesize = int.from_bytes(data, 'big')  # 수신된 파일 크기 정보를 정수로 변환
    print('server:', filesize)

    rx_size = 0
    f = open(filename, 'wb')  # 파일을 쓰기 모드로 열기
    while rx_size < filesize:  # 파일 크기만큼 데이터 수신
        data = s.recv(BUF_SIZE)
        if not data:
            break  # 더 이상 데이터가 없으면 종료
        f.write(data)  # 수신된 데이터를 파일에 쓰기
        rx_size += len(data)
    if rx_size < filesize:
        s.close()
        sys.exit()  # 파일 전체를 수신하지 못한 경우

    print('Download complete')  # 파일 다운로드 완료 메시지 출력
    s.send(b'Bye')  # 서버에 'Bye' 메시지 전송

    f.close()  # 파일 닫기
    s.close()  # 연결 종료
