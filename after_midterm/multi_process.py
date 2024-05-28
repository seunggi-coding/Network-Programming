from multiprocessing import Process  # 프로세스 생성을 위한 multiprocessing 모듈 임포트
import os  # 프로세스 ID와 부모 프로세스 ID를 얻기 위한 os 모듈 임포트

# 프로세스 정보를 출력하는 함수
def info(title):
    print(title)  # 제목 출력
    print('parent process:', os.getppid())  # 부모 프로세스 ID 출력
    print('process id:', os.getpid())  # 현재 프로세스 ID 출력
    
# 자식 프로세스에서 실행될 함수
def f(name):
    info('function f')  # 프로세스 정보 출력
    print('hello', name)  # 인사말 출력
    
if __name__ == '__main__':  # 메인 프로세스에서만 실행
    info('main line')  # 메인 프로세스 정보 출력
    p = Process(target=f, args=('bob',))  # 자식 프로세스 생성, 함수 f와 인자 'bob'을 전달
    p.start()  # 자식 프로세스 시작
    p.join()  # 자식 프로세스가 종료될 때까지 대기
