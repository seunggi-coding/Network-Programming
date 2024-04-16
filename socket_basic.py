# socket 모듈 사용하기
import socket

# 현재 실행 중인 시스템의 호스트 이름을 가져옵니다.
name = socket.gethostname()
print(name)  # 현재 시스템의 호스트 이름 출력

# 주어진 호스트 이름에 대한 IP 주소를 가져옵니다.
addr = socket.gethostbyname(name)
print(addr)  # 호스트 이름에 해당하는 IP 주소 출력

# 'homepage.sch.ac.kr' 도메인 이름에 대한 IP 주소를 가져옵니다.
print(socket.gethostbyname('homepage.sch.ac.kr'))

# 'homepage.sch.ac.kr' 도메인 이름에 대한 IP 주소, 별칭, IP 주소 목록을 가져옵니다.
# 이는 도메인이 여러 IP 주소를 가질 때 유용합니다.
print(socket.gethostbyname_ex('homepage.sch.ac.kr'))

# 주어진 IP 주소에 대한 호스트 이름, 별칭, IP 주소 목록을 가져옵니다.
# 이 함수는 IP 주소를 통해 해당 서버의 정보를 얻고 싶을 때 사용됩니다.
print(socket.gethostbyaddr('220.69.189.98'))

# 주어진 이름에 대한 완전한 도메인 이름(FQDN)을 가져옵니다.
# FQDN은 도메인 이름이 완전하게 표시된 형태입니다.
print(socket.getfqdn('220.69.189.98'))  # IP 주소에 대한 FQDN
print(socket.getfqdn('www.daum.net'))   # 도메인 이름에 대한 FQDN
print(socket.getfqdn('www.google.com'))  # 다른 도메인 이름에 대한 FQDN

# socket 모듈의 주요 함수 설명:
# gethostname() - 현재 로컬 시스템의 호스트 이름을 반환합니다.
# gethostbyname(hostname) - 주어진 호스트 이름에 대한 IPv4 주소를 문자열 형태로 반환합니다.
# gethostbyname_ex(hostname) - 주어진 호스트 이름에 대한 호스트 이름, 별칭 리스트, 사용 가능한 IP 주소 리스트를 반환합니다.
# gethostbyaddr(ip_address) - 주어진 IP 주소에 대한 호스트 이름, 별칭 리스트, IP 주소 리스트를 반환합니다.
# getfqdn(name) - 주어진 도메인 이름 또는 IP 주소에 대한 완전한 도메인 이름(FQDN)을 반환합니다.
