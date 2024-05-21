import threading

def prtSquare(num):
    # num의 제곱을 출력
    print("Square {}".format(num**2))

def prtCube(num):
    # num의 세제곱을 출력
    print("Cube: {}".format(num**3))
    
# prtSquare 함수를 실행하는 스레드 t1 생성, 인자로 10 전달
t1 = threading.Thread(target=prtSquare, args=(10,))
# prtCube 함수를 실행하는 스레드 t2 생성, 인자로 10 전달
t2 = threading.Thread(target=prtCube, args=(10,))

# t1 스레드 시작
t1.start()
# t2 스레드 시작
t2.start()

# t1 스레드가 종료될 때까지 대기
t1.join()
# t2 스레드가 종료될 때까지 대기
t2.join()

# 모든 스레드가 종료된 후 "Done" 출력
print("Done")
