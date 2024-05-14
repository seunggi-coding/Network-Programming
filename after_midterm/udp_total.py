import argparse
import socket
import random
from datetime import datetime

BUFF_SIZE = 1024  # 버퍼의 크기 설정

def Server(ipaddr, port):
    # 서버 함수
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP 소켓 생성
    sock.bind((ipaddr, port))  # 주어진 IP 주소와 포트에 소켓 바인드
    print('Waiting in {}...'.format(sock.getsockname()))  # 서버가 시작된 주소와 포트 출력
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)  # 클라이언트로부터 데이터를 받아옴
        if random.random() < prob:  # 데이터 드롭 확률에 따라 드롭 여부 결정
            print('Message from {} is lost.'.format(addr))  # 데이터가 드롭된 경우 출력
            continue
        print('{} client message {!r}'.format(addr, data.decode()))  # 드롭되지 않은 데이터 출력
        text = 'The length is {} bytes.'.format(len(data))  # 받은 데이터의 길이를 텍스트로 변환
        sock.sendto(text.encode(), addr)  # 클라이언트에게 데이터 길이를 전송

def Client(hostname, port):
    # 클라이언트 함수
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP 소켓 생성
    index = 1  # 보낸 메시지 번호
    time = 0.1  # 초 단위 시간 변수
    while True:
        data = str(datetime.now())  # 현재 시간을 문자열로 변환
        sock.sendto(data.encode(), (hostname, port))  # 서버에게 현재 시간 데이터 전송
        print('({}) Waiting for {} sec'.format(index, time))  # 클라이언트가 기다리는 시간 출력
        sock.settimeout(time)  # 소켓의 타임아웃 시간 설정
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)  # 서버로부터 데이터를 받아옴
        except socket.timeout:  # 서버로부터의 응답이 없을 때
            time *= 2  # 대기 시간 두 배로 늘림
            if time > 2.0:  # 대기 시간이 2초를 초과하면 패킷을 잃어버린 것으로 판단
                print('{}th packet is lost'.format(index))  # 잃어버린 패킷 번호 출력
                if index >= sending_counts:  # 패킷 전송 횟수를 초과하면 종료
                    break
            index += 1  # 패킷 번호 증가
            time = 0.1  # 대기 시간 초기화
        else:
            print('Server reply: {!r}'.format(data.decode()))  # 서버로부터의 응답 출력
            if index >= sending_counts:  # 패킷 전송 횟수를 초과하면 종료
                break
            index += 1  # 패킷 번호 증가
            time = 0.1  # 대기 시간 초기화

if __name__ == '__main__':
    mode = {'c': Client, 's': Server}  # 클라이언트와 서버 함수를 딕셔너리에 저장
    parser = argparse.ArgumentParser(description='Send and receive UDP packets with setting drop probability')
    parser.add_argument('role', choices=mode, help='which role to take between server and client')  # 역할 선택 인자
    parser.add_argument('-s', default='localhost', help='server that client sends to')  # 서버 주소 인자
    parser.add_argument('-p', type=int, default=2500, help='UDP port (default:2500)')  # 포트 번호 인자
    parser.add_argument('-prob', type=float, default=0, help='dropping probability (0~1)')  # 드롭 확률 인자
    parser.add_argument('-count', type=int, default=10, help='number of sending packets')  # 패킷 전송 횟수 인자
    args = parser.parse_args()  # 인자 파싱
    prob = args.prob  # 드롭 확률 변수 설정
    sending_counts = args.count  # 패킷 전송 횟수 변수 설정
    if args.role == 'c':  # 클라이언트 모드일 경우
        mode[args.role](args.s, args.p)  # 클라이언트 함수 실행
    else:  # 서버 모드일 경우
        mode[args.role]('', args.p)  # 서버 함수 실행
