from socket import *
import random

BUFF_SIZE = 1024
port = 5555

c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('localhost', port))
print('Listening...')

for i in range(10):
    time = 0.1
    data = 'Hello, IoT'
    
    while True:
        if type(data) is str:
            c_sock.send(data.encode())
        else:
            c_sock.send(data)
        print('Packet({}): Waiting up to {} seconds for ack'.format(i, time))
        c_sock.settimeout(time)
        try:
            data = c_sock.recv(BUFF_SIZE)
        except timeout:
            time *= 2
            if time > 2.0:
                break
        else:
            if type(data) is str:
                print('Response', data)
            else:
                print('Response', data.decode())
            break