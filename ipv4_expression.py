# IPv4 주소 표현

import binascii
import socket
import sys
import socket

# inet_aton() 함수 사용 예제
# 점 표기(dot notation)의 IP 주소를 32비트 패킹된 바이너리 형태로 변환합니다.
ip_address = '192.168.0.1'
packed_ip = socket.inet_aton(ip_address)
print(f"{ip_address}의 패킹된 바이너리 형태: {packed_ip}")

# inet_ntoa() 함수 사용 예제
# 32비트 패킹된 바이너리 형태의 IP 주소를 점 표기(dot notation)의 문자열로 변환합니다.
unpacked_ip = socket.inet_ntoa(packed_ip)
print(f"패킹된 바이너리 형태의 IP 주소 {packed_ip}를 점 표기 형태로 변환: {unpacked_ip}")
