from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input("계산을 위한 수식을 입력하세요. ex) 20 + 17 or q를 입력해 종료하세요 : ")
    if msg == 'q':
        break
    s.send(msg.encode())
    result = s.recv(1024).decode()
    print("Received result: ", result)

s.close()
