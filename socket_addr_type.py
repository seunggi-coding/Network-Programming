from socket import * 
s1 = socket(AF_INET, SOCK_STREAM)
s2 = socket(AF_INET, SOCK_DGRAM)
print(s1, s2)