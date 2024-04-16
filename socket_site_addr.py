# 여러 사이트의 IP 주소를 확인하는 프로그램
# 여러 사이트의 IP 주소를 확인하는 프로그램
import socket  # socket 모듈을 불러옵니다.

# 조회할 호스트 이름들을 선언합니다. 이는 세트(Set) 형태로 저장되어 있으며, 중복을 허용하지 않습니다.
HOSTS = {
    'www.sch.ac.kr',         # 순천향대학교 메인 페이지
    'homepage.sch.ac.kr',    # 순천향대학교 홈페이지
    'www.daum.net',          # 다음 포털 사이트
    'www.google.com',        # 구글 검색 사이트
    'iot'                    # 존재하지 않을 수 있는 호스트 이름 예시
}

# HOSTS에 저장된 각 호스트 이름에 대해 반복합니다.
for host in HOSTS:
    try:
        # 주어진 호스트 이름에 대한 IP 주소를 조회합니다.
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg:
        # 호스트 이름 조회 중 오류가 발생한 경우, 오류 메시지를 출력합니다.
        # 예를 들어, 호스트 이름이 잘못되었거나, 네트워크에 문제가 있는 경우에 해당합니다.
        print('{} : {}'.format(host, msg))
