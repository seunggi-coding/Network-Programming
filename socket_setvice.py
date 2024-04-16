# 인터넷 서비스 정보 알아내기
# 인터넷 서비스 정보 알아내기
import socket  # socket 모듈을 불러옵니다.

# getservbyname() 함수를 사용하여 특정 서비스의 표준 포트 번호를 알아냅니다.
# 이 함수는 서비스 이름을 문자열로 받아 해당 서비스가 사용하는 포트 번호를 반환합니다.
print(socket.getservbyname('http'))  # HTTP 서비스의 포트 번호 (일반적으로 80)
print(socket.getservbyname('ssh'))   # SSH 서비스의 포트 번호 (일반적으로 22)
print(socket.getservbyname('https')) # HTTPS 서비스의 포트 번호 (일반적으로 443)
print(socket.getservbyname('ftp'))   # FTP 서비스의 포트 번호 (일반적으로 21)

# getservbyport() 함수를 사용하여 특정 포트 번호에 대응하는 서비스 이름을 알아냅니다.
# 이 함수는 포트 번호를 정수로 받아 해당 포트를 사용하는 서비스의 이름을 반환합니다.
print(socket.getservbyport(80))  # 포트 번호 80에 해당하는 서비스 이름 (HTTP)
print(socket.getservbyport(25))  # 포트 번호 25에 해당하는 서비스 이름 (SMTP)

# 다양한 포트 번호에 대해 서비스 이름을 조회하고 이를 URL 형식으로 출력합니다.
for port in [80, 443, 21, 25, 143, 993, 110, 995]:
    # getservbyport() 함수를 사용해 포트 번호에 해당하는 서비스 이름을 가져온 후,
    # 이를 URL의 프로토콜 부분으로 사용합니다.
    url = '{}://example.co.kr/'.format(socket.getservbyport(port))
    print('{:4d}'.format(port), url)
    # 포트 번호와 해당 포트를 사용하는 서비스의 URL을 출력합니다.
    
# 이 코드는 네트워크 프로그래밍에서 자주 사용되는 서비스 이름과 포트 번호를 조회하는 방법을 보여줍니다.
# 이를 통해 프로그래머는 서비스의 포트 번호나 이름을 직접 기억하지 않아도 됩니다.
