import socket
import threading

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            break

server_addr = ('localhost', 2500)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_addr)

my_id = input('Enter your ID: ')
sock.send(f'[{my_id}]'.encode())

th = threading.Thread(target=receive_messages, args=(sock,), daemon=True)
th.start()

while True:
    msg = input()
    if msg.lower() == 'quit':
        sock.send(f'[{my_id}] has left the chat.'.encode())
        break
    sock.send(f'[{my_id}] {msg}'.encode())
sock.close()
