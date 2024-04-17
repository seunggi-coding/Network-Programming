# x의 n제곱을 구하는 프로그램

# 사용자로부터 실수 x를 입력받음
x = float(input('Type x : '))
# 사용자로부터 정수 n을 입력받음
n = int(input('Type n : '))

# 곱셈 결과를 저장할 변수 prod를 1로 초기화
prod = 1
# 1부터 n까지 반복
for i in range(1, n+1):
    # 현재 prod 값에 x를 곱하여 prod를 업데이트
    prod = prod * x 
# 계산된 최종 prod 값을 출력
print(prod)
