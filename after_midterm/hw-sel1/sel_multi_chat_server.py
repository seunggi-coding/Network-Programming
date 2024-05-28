import socket, select

socks = []
BUFFER = 1024
PORT = 2500

s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)
print(f"{PORT}에서 접속 대기 중...")

while True:
    r_sock, w_sock, e_sock = select.select(socks, [], [])
    
    for s in r_sock:
        if s == s_sock:
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print(f"새로운 클라이언트 {addr}가 연결되었습니다.")
        else:
            try:
                data = s.recv(BUFFER)
                if not data:
                    s.close()
                    socks.remove(s)
                    print(f"클라이언트 {addr}가 연결을 종료했습니다.")
                    continue
                
                addr = s.getpeername()
                message = data.decode().strip()
                print(f"{addr}: {message}")
                
                if message.lower() == 'quit':
                    print(f"클라이언트 {addr}가 종료를 요청했습니다.")
                    s.close()
                    socks.remove(s)
                    continue
                else:
                    for client in socks:
                        if client != s and client != s_sock:
                            client.send(data)
            except ConnectionResetError:
                s.close()
                socks.remove(s)
                print(f"클라이언트 {addr}와의 연결이 끊겼습니다.")
