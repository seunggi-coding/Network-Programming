from socket import *
import argparse

s = socket(AF_INET, SOCK_STREAM)

parser = argparse.ArgumentParser()
parser.add_argument('-s', default='localhost')
parser.add_argument('-p', type=int, default=2500)
""" 위의 두 줄은 아래 두 줄과 같은 의미입니다. 아래의 두 줄과 같이 작성했다면 
s.connect((args.address, args.port))라고 작성해야 함.
parser.add_argument('--address', '-s', default='localhost')
parser.add_argument('--port', '-p', type=int, default=2500)
 """
args = parser.parse_args()

s.connect((args.s, args.p))
print("Connected to", args.s, args.p)

while True:
    msg = input("Message to send: ")
    if msg == 'q':
        break
    s.send(msg.encode())
    data = s.recv(1024)
    
    if not data:
        break
    print('Received message:', data.decode())

s.close()