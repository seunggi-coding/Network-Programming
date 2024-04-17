# 전역 변수 선언
number = 10

# 전역 변수의 값을 변경하는 함수
def update_number():
    global number  # 전역 변수 'number'를 사용하겠다고 선언
    number = 20    # 전역 변수의 값을 변경

# 함수 호출 전 전역 변수의 값 확인
print(f"함수 호출 전 number의 값: {number}")  # 출력: 함수 호출 전 number의 값: 10

# 함수 호출
update_number()

# 함수 호출 후 전역 변수의 값 확인
print(f"함수 호출 후 number의 값: {number}")  # 출력: 함수 호출 후 number의 값: 20
