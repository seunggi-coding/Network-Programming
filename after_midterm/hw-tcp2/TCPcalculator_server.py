from socket import *

def calculate(expression):
    expression = expression.replace(" ", "")
    result = eval(expression)
    return str(round(result, 1))

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print("Connection waiting...")

while True:
    client, addr = s.accept()
    print("Connected from", addr)
    
    while True:
        data = client.recv(1024)
        if not data:
            break
        result = calculate(data.decode())
        client.send(result.encode())
    
    client.close()
