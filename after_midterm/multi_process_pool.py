from multiprocessing import Pool  # Pool 클래스를 사용하기 위해 multiprocessing 모듈에서 Pool 임포트

# 주어진 숫자의 제곱을 반환하는 함수
def f(x):
    return x*x

if __name__ == '__main__':  # 메인 모듈에서 실행될 때
    with Pool(5) as p:  # 프로세스 풀(Pool)을 생성하고, 동시에 실행될 프로세스의 수를 5로 설정
        # p.map 함수를 사용하여 리스트 [1, 2, 3]의 각 요소를 함수 f에 매핑(적용)
        # 이 과정은 병렬로 수행되며, 각 숫자는 제곱됨
        # 예: f(1) -> 1, f(2) -> 4, f(3) -> 9
        print(p.map(f, [1, 2, 3]))  # 결과 [1, 4, 9] 출력

# 이 코드는 multiprocessing 모듈의 Pool을 사용하여 병렬 프로그래밍을 단순화하는 예제임.
# Pool 객체를 사용하면, 여러 입력값에 대해 함수를 병렬로 실행할 수 있으며,
# 이는 데이터 처리와 같이 반복적이고 독립적인 작업을 병렬로 처리할 때 유용함.
# with 구문을 사용하여 Pool을 사용하는 동안 Pool이 자동으로 종료되고 리소스가 정리되도록 함.
