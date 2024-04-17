import ipaddress

# ip_address() 사용 예제
# '192.168.1.1'에 대한 IP 주소 객체 생성
ip = ipaddress.ip_address('192.168.1.1')
print(ip)  # IP 주소 출력
# 출력: 192.168.1.1

# ip_network() 사용 예제
# '192.168.1.0/24' 네트워크에 대한 객체 생성, 마지막에 strict=False를 추가하여 네트워크 주소가 아닌 주소로도 네트워크 객체를 생성할 수 있음

# strict 파라미터를 명시적으로 사용하지 않는 예제
# '192.168.1.0/24' 네트워크에 대한 객체 생성
# 이 경우 strict는 기본값인 True를 사용합니다.
# 따라서 '192.168.1.0/24'는 네트워크의 첫 번째 주소여야 합니다.
network = ipaddress.ip_network('192.168.1.0/24')
print(network)  # 네트워크 주소 출력
# 출력: 192.168.1.0/24

try:
    network_strict_true = ipaddress.ip_network('192.168.1.5/24', strict=True)
    print(network_strict_true)
except ValueError as e:
    print(e)  # 네트워크 주소가 네트워크의 첫 번째 주소가 아닐 때 발생하는 에러 메시지 출력

network = ipaddress.ip_network('192.168.1.0/24', strict=False)
print(network)  # 네트워크 주소 출력
# 출력: 192.168.1.0/24

# hosts() 사용 예제
# 생성된 네트워크의 호스트들 나열
for host in network.hosts():
    print(host)
# 출력: 192.168.1.1 부터 192.168.1.254 까지의 주소를 줄 단위로 출력


# 위의 예제에서 ip_address() 함수는 주어진 문자열을 IP 주소 객체로 변환합니다.
# 이 객체는 IP 주소와 관련된 다양한 정보와 연산을 수행할 수 있습니다.
# ip_network() 함수는 주어진 네트워크 주소 문자열로부터 네트워크 객체를 생성합니다.
# 이 객체는 네트워크에 속한 IP 주소들, 네트워크의 마스크 길이, 네트워크 주소 등의 정보를 제공합니다.
# hosts() 메소드는 해당 네트워크에 속하는 모든 호스트의 IP 주소를 순회할 수 있는 반복자를 반환합니다.
# 이를 통해 네트워크 내의 모든 가능한 호스트 주소를 나열할 수 있습니다.
