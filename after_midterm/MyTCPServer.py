class TCPServer:
    def __init__(self, port):
        import socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', port))
        self.sock.listen(5)
    def Accept(self):
        self.c_sock, self.c_addr = self.sock.accept()
        return self.c_sock, self.c_addr
    
if __name__ == '__main__':
    server = TCPServer(8888)
    c, addr = server.Accept()
    print("connected by ", addr)
    c.send(b"Hello Client")
    c.close()