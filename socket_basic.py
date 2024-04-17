# socket 모듈의 주요 함수 설명:
# gethostname() - 현재 로컬 시스템의 호스트 이름을 반환합니다.
# gethostbyname(hostname) - 주어진 호스트 이름에 대한 IPv4 주소를 문자열 형태로 반환합니다.
# gethostbyname_ex(hostname) - 주어진 호스트 이름에 대한 호스트 이름, 별칭 리스트, 사용 가능한 IP 주소 리스트를 반환합니다.
# gethostbyaddr(ip_address) - 주어진 IP 주소에 대한 호스트 이름, 별칭 리스트, IP 주소 리스트를 반환합니다.
# getfqdn(name) - 주어진 도메인 이름 또는 IP 주소에 대한 완전한 도메인 이름(FQDN)을 반환합니다.

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
print(socket.gethostbyname_ex('homepage.sch.ac.kr'))

# 주어진 IP 주소에 대한 호스트 이름, 별칭, IP 주소 목록을 가져옵니다.
print(socket.gethostbyaddr('220.69.189.98'))

# 주어진 이름에 대한 완전한 도메인 이름(FQDN)을 가져옵니다.
print(socket.getfqdn('220.69.189.98'))
print(socket.getfqdn('www.daum.net'))
print(socket.getfqdn('www.google.com'))

# getservbyname() 함수 사용 예시
# 'http' 서비스에 대한 포트 번호를 가져옵니다.
http_port = socket.getservbyname('http')
print(http_port)  # 기본적으로 80 포트를 반환합니다.

# 'https' 서비스에 대한 포트 번호를 가져옵니다.
https_port = socket.getservbyname('https')
print(https_port)  # 기본적으로 443 포트를 반환합니다.

# getservbyport() 함수 사용 예시
# 포트 번호 80에 대한 서비스 이름을 가져옵니다.
service_name_http = socket.getservbyport(80)
print(service_name_http)  # 기본적으로 'http'를 반환합니다.

# 포트 번호 443에 대한 서비스 이름을 가져옵니다.
service_name_https = socket.getservbyport(443)
print(service_name_https)  # 기본적으로 'https'를 반환합니다.