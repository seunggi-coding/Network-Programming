""" 자신이 사용하고 있는 PC의  IP 주소를 찾아 출력하는 프로그램을 작성하시오.
호스트에 대한 더 많은 정보에 액세스하려면 gethostbyname_ex(hostname)를 사용할 수 있다. 
이 함수는 호스트에 대한 정보를 (hostname, aliaslist, ipaddrlist) 튜플로 반환한다. hostname은 
표준 호스트 이름，aliaslist는 호스트 별칭 리스트，ipaddrlist는 호스트에 사용 가능한 모든 
IP 주소 리스트를 나타낸다. """
import socket

def find_my_ip():
    # 현재 PC의 호스트 이름을 가져옵니다.
    hostname = socket.gethostname()
    # gethostbyname() 함수를 사용하여 현재 PC의 IP 주소를 가져옵니다.
    ip_address = socket.gethostbyname(hostname)
    print(f"Your Computer IP Address is: {ip_address}")

find_my_ip()

""" gethostbyname_ex()  함수를 이용하여 네이버  호스트(www.naver.com)에  대한 정보를 찾아보자 """
def get_host_info_ex(hostname):
    try:
        # gethostbyname_ex() 함수를 사용하여 호스트 정보를 가져옵니다.
        hostname, aliaslist, ipaddrlist = socket.gethostbyname_ex(hostname)
        
        # 결과 출력
        print(f"Host Name: {hostname}")
        print(f"Alias List: {aliaslist}")
        print(f"IP Address List: {ipaddrlist}")
    except socket.gaierror as error:
        print(f"Error fetching the host information: {error}")

get_host_info_ex("www.naver.com")

""" ‘www.ulsan.ac.kr’의  IP 주소를 찾아내고 ‘147.46.10.58‘의  문자열 주소를 찾아보자. """
def find_ip_and_host():
    # 'www.ulsan.ac.kr'의 IP 주소 찾기
    ulsan_ip = socket.gethostbyname('www.ulsan.ac.kr')
    print(f"'www.ulsan.ac.kr' IP Address: {ulsan_ip}")

    # '147.46.10.58'의 호스트 이름 찾기
    try:
        host_name = socket.gethostbyaddr('147.46.10.58')
        print(f"Host name for '147.46.10.58': {host_name[0]}")
    except socket.herror:
        print("Unable to find the Host name for '147.46.10.58'")

find_ip_and_host()

# socket 모듈의 gethostbynameO 함수의 사용법을 알아보자. 또한 ‘SOCK_STREAM’과 ‘SOCK_DGRAM’의 
# 속성값을 확인해  보자.  이들 문자 상수는 어떤 유형을 나타내는가?
hostname = 'www.example.com'
ip_address = socket.gethostbyname(hostname)
print(f'IP 주소: {ip_address}')
""" SOCK_STREAM과 SOCK_DGRAM
socket 모듈에서 SOCK_STREAM과 SOCK_DGRAM은 소켓 유형을 지정하는 데 사용되는 정수 상수입니다.

SOCK_STREAM: 이 속성값은 연결 지향형 소켓을 나타냅니다. TCP(Transmission Control Protocol)와 함께 사용되며, 데이터가 순서대로 도착하고 신뢰성 있는 데이터 전송을 보장합니다. 스트림 소켓은 두 호스트 간에 안정적인 양방향 통신을 구현하는 데 적합합니다.

SOCK_DGRAM: 이 속성값은 비연결 지향형 소켓을 나타냅니다. UDP(User Datagram Protocol)와 함께 사용되며, 데이터의 신뢰성을 보장하지 않고 순서도 보장하지 않습니다. 대신, 전송 속도가 빠르며 오버헤드가 낮습니다. 데이터그램 소켓은 실시간 애플리케이션(예: 비디오 스트리밍, 게임)에 주로 사용됩니다. """

# getaddrinfoO 함수를 사용하여 ‘http://www.naver.com’에 대한 정보를 찾아보자.  이 사이트는 몇 개의 
# IP 주소를 가지고 있는가? 또 각각 주소 유형，소켓 유형，전송 프로토콜은 무엇인가?
hostname = 'www.naver.com'

# getaddrinfo() 호출
try:
    # 서비스 이름이나 포트 번호를 지정하지 않고 AF_UNSPEC로 주소 체계를 모두 받아옵니다.
    result = socket.getaddrinfo(hostname, None, proto=socket.IPPROTO_TCP)
    
    print(f"{hostname}는/은 다음의 IP 주소를 가지고 있습니다:")
    for info in result:
        # 각 정보를 출력합니다.
        address_family, socket_type, proto, canonname, sockaddr = info
        print(f"주소 유형: {socket.getnameinfo((sockaddr[0], 0), 0)[0]}, 소켓 유형: {socket_type}, 전송 프로토콜: {proto}, 주소: {sockaddr}")
except socket.gaierror as error:
    print(f"주소 정보를 가져오는데 실패했습니다: {error}")
    
# socket 모듈의 inet_ntoa()와 inet_aton() 함수는 IP 주소와 관련된 변환 작업을 수행합니다.
# 도트(.)로 구분된 IPv4 주소
ip_addr_str = "192.168.0.1"

# inet_aton() 함수를 사용하여 이진 형식으로 변환
packed_ip = socket.inet_aton(ip_addr_str)

print("Packed IP:", packed_ip)

# 32비트 포장된 이진 형태의 IPv4 주소
packed_ip = b'\xC0\xA8\x00\x01'

# inet_ntoa() 함수를 사용하여 도트(.) 구분 형식으로 변환
ip_addr_str = socket.inet_ntoa(packed_ip)

print("IP Address String:", ip_addr_str)

# socket 모듈의 ntohl(), ntohs(), htonl(), htons() 함수는 네트워크 바이트 순서와 호스트 바이트 순서 간의 변환을 수행하는 데 사용됩니다
# 호스트 바이트 순서의 32비트 정수
host_long = 0x12345678

# 호스트 바이트 순서의 16비트 정수
host_short = 0x1234

# htonl: 호스트에서 네트워크 바이트 순서(long)로 변환
network_long = socket.htonl(host_long)

# htons: 호스트에서 네트워크 바이트 순서(short)로 변환
network_short = socket.htons(host_short)

# ntohl: 네트워크에서 호스트 바이트 순서(long)로 변환
converted_host_long = socket.ntohl(network_long)

# ntohs: 네트워크에서 호스트 바이트 순서(short)로 변환
converted_host_short = socket.ntohs(network_short)

print(f"Original Host Long: {hex(host_long)}, Converted to Network: {hex(network_long)}, Back to Host: {hex(converted_host_long)}")
print(f"Original Host Short: {hex(host_short)}, Converted to Network: {hex(network_short)}, Back to Host: {hex(converted_host_short)}")

