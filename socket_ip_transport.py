# ip 변환 함수
import binascii
import socket
import sys

# 주어진 IP 주소 목록을 반복 처리
for string_address in ['114.71.220.95']:
    # inet_aton 함수를 사용하여 점으로 구분된 IPv4 주소를 32비트의 네트워크 바이트 순서로 포장된 4바이트의 문자열로 변환
    packed = socket.inet_aton(string_address)
    print('Original: ', string_address)  # 원래의 IP 주소를 출력
    print('Packed: ', binascii.hexlify(packed))  # 포장된 데이터를 16진수로 변환하여 출력
    print('Unpacked: ', socket.inet_ntoa(packed))  # 포장 해제된 데이터를 원래의 점으로 구분된 IPv4 주소로 변환하여 출력

# inet_aton 함수 설명:
# inet_aton은 "인터넷 주소를 숫자로"라는 의미로, 점으로 구분된 IPv4 주소를 32비트의 네트워크 바이트 순서(bin)으로 포장된 4바이트의 문자열로 변환합니다.
# 이 함수는 주로 소켓 프로그래밍에서 IP 주소를 처리할 때 사용됩니다.

# inet_ntoa 함수 설명:
# inet_ntoa는 "숫자를 인터넷 주소로"라는 의미로, 32비트의 네트워크 바이트 순서로 포장된 4바이트의 문자열(IP 주소)를 점으로 구분된 IPv4 주소로 변환합니다.
# 이 함수는 주로 네트워크 프로그래밍에서 바이너리 형태의 IP 주소를 사람이 읽을 수 있는 형태로 변환할 때 사용됩니다.
