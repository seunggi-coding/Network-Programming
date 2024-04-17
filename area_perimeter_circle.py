# 1~n까지의 합을 계산하는 함수

import math

# 원의 면적을 구하는 함수
def cir_area(r):
    return math.pi * r ** 2

# 원의 둘레를 구하는 함수
def cir_circum(r):
    return 2 * math.pi * r

# 반지름이 3.5cm인 원의 면적과 둘레 계산
radius = 3.5
area = cir_area(radius)
circumference = cir_circum(radius)

# 결과 출력 (소수점 아래 첫 자리까지)
print(f"반지름이 {radius}cm인 원의 면적: {area:.1f}cm²")
print(f"반지름이 {radius}cm인 원의 둘레: {circumference:.1f}cm")
