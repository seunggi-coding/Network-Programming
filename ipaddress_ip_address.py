# ipaddress 모듈 사용
import ipaddress
addr4 = ipaddress.ip_address('192.0.2.1')
print(addr4)

addr6 = ipaddress.ip_address('2001:A8::1')
print(addr6)

print(addr4.version)
print(addr6.version)

net = ipaddress.ip_network('114.71.220.0/24')
addr = ipaddress.ip_address('114.71.220.95')
print(addr in net)

addr = ipaddress.ip_address('192.168.0.1')
print(addr in net)