from socket import *
import random
import time

BUFFSIZE = 1024
port = 3333

c_sock = socket(AF_INET, SOCK_DGRAM)
server_addr = ('localhost', port)

while True:
    msg = input('-> ')
    reTx = 0
    while reTx <= 5:
        resp = str(reTx) + ' ' + msg
        c_sock.sendto(resp.encode(), server_addr)
        c_sock.settimeout(2)
        try:
            data, addr = c_sock.recvfrom(BUFFSIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break
    
    
    c_sock.settimeout(None)
    while True:
        data, addr = c_sock.recvfrom(BUFFSIZE)
        if random.random() <= 0.5:
            continue
        else:
            c_sock.sendto(b'ack', addr)
            print('<- ', data.decode())
            break
