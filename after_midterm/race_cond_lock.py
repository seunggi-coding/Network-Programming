import threading

# 전역 변수 x를 선언합니다. 이 변수는 스레드에 의해 접근 및 수정됩니다.
x = 0

def increment():
    # increment 함수는 전역 변수 x를 수정합니다.
    global x
    x += 1  # x의 값을 1 증가시킵니다.
    
def thread_task(lock):
    # thread_task 함수는 increment 함수를 300,000번 호출합니다.
    for _ in range(300000):
        lock.acquire()  # lock을 획득합니다.
        increment()
        lock.release()  # lock을 해제합니다.

def main_task():
    global x  # 함수 내에서 전역 변수 x를 사용하기 위해 선언합니다.
    x = 0  # 각 실행마다 x를 0으로 초기화합니다.
    
    lock = threading.Lock()  # Lock 객체를 생성합니다.
    
    # 두 개의 스레드(t1, t2)를 생성하고, 각각 thread_task 함수를 실행합니다.
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))
    
    # 스레드를 시작합니다.
    t1.start()
    t2.start()
    
    # 두 스레드가 종료될 때까지 기다립니다.
    t1.join()
    t2.join()

# main_task 함수를 10번 반복 실행합니다.
for i in range(10):
    main_task()
    # 각 반복 후 x의 값이 얼마인지 출력합니다.
    # 이론적으로는 x가 600,000이 되어야 하지만, 경쟁 상태(race condition)로 인해
    # 그 값이 달라질 수 있습니다.
    print("Iteration {0}: x = {1}".format(i, x))
