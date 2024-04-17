# 바이트 순서 변환
import socket

# 호스트 바이트 순서의 32비트 정수 예제
host_order_32 = 0x12345678
# 호스트 바이트 순서의 16비트 정수 예제
host_order_16 = 0x1234

""" htonl()과 htons() 메서드는 호스트 바이트 순서에서 네트워크 바이트 순서로 변환하는 예제 (빅 엔디언으로 변환해서 전송) """
# htonl: 호스트 -> 네트워크 (32비트)
network_order_32 = socket.htonl(host_order_32)
print(f"32비트 호스트 -> 네트워크: {hex(host_order_32)} -> {hex(network_order_32)}")

# htons: 호스트 -> 네트워크 (16비트)
network_order_16 = socket.htons(host_order_16)
print(f"16비트 호스트 -> 네트워크: {hex(host_order_16)} -> {hex(network_order_16)}")

""" ntohl()과 ntohs() 메서드는 네트워크 바이트 순서에서 호스트 바이트 순서로 변환하는 기능을 수행합니다. 
이 변환 과정에서 네트워크 바이트 순서(빅 엔디언)에서 호스트의 바이트 순서로 변환됩니다. """
# ntohl: 네트워크 -> 호스트 (32비트)
converted_back_32 = socket.ntohl(network_order_32)
print(f"32비트 네트워크 -> 호스트: {hex(network_order_32)} -> {hex(converted_back_32)}")

# ntohs: 네트워크 -> 호스트 (16비트)
converted_back_16 = socket.ntohs(network_order_16)
print(f"16비트 네트워크 -> 호스트: {hex(network_order_16)} -> {hex(converted_back_16)}")
