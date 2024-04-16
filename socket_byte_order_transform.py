# 바이트 순서 변환 함수

import socket

a = 1234
print(hex(a))  # 변수 a의 값을 16진수로 출력합니다. 이 경우 1234의 16진수 표현은 '0x4d2'입니다.

# htons() 함수를 사용하여 호스트 바이트 순서에서 네트워크 바이트 순서로 16비트 수를 변환합니다.
b = socket.htons(a)
print(hex(b))  # 변환된 값을 16진수로 출력합니다. 이 값은 시스템의 엔디언에 따라 달라질 수 있습니다.

# ntohs() 함수를 사용하여 네트워크 바이트 순서에서 호스트 바이트 순서로 16비트 수를 변환합니다.
c = socket.ntohs(b)
print(hex(c))  # 다시 원래의 값(1234)으로 변환된 값을 16진수로 출력합니다. '0x4d2'가 출력됩니다.

# htons(x)와 ntohs(x) 함수는 16비트(2바이트) 수의 바이트 순서를 변환하는 데 사용됩니다.
# htonl(x)와 ntohl(x) 함수는 32비트(4바이트) 수의 바이트 순서를 변환하는 데 사용됩니다.

# 예제:
# htonl(x)와 ntohl(x) 사용 예제
ip_address = 0x12345678  # 32비트 수
network_order = socket.htonl(ip_address)  # 호스트에서 네트워크 바이트 순서로 변환
host_order = socket.ntohl(network_order)  # 네트워크에서 호스트 바이트 순서로 변환
print("Original:", hex(ip_address))  # 원본 32비트 수를 16진수로 출력
print("Network order:", hex(network_order))  # 네트워크 바이트 순서로 변환된 값을 16진수로 출력
print("Converted back to host order:", hex(host_order))  # 다시 호스트 바이트 순서로 변환된 값을 16진수로 출력
