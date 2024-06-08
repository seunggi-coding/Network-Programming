import time

def get_user(name):
    print('사용자 {!r} 정보 조회중...'.format(name))
    time.sleep(1)
    print('사용자 {!r} 정보 조회 완료'.format(name))
    
def main():
    start = time.time()
    get_user('Jeon')
    get_user('Yun')
    get_user('Kim')
    get_user('Song')
    end = time.time()
    print('총 소요 시간: {}초'.format(end-start))
    
main()