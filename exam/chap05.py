# 튜플을 이용하여 정사각형의 한 변의 길이가 주어졌을 때, 정사각형의 넓이와 둘레를 한꺼번에 반환하는 함수를 작성하라.
def square_properties(side_length):
    """
    정사각형의 한 변의 길이를 입력받아,
    해당 정사각형의 넓이와 둘레를 계산하여 반환하는 함수
    
    Parameters:
    side_length (float): 정사각형의 한 변의 길이
    
    Returns:
    tuple: (정사각형의 넓이, 정사각형의 둘레)
    """
    # 정사각형의 넓이 계산
    area = side_length ** 2
    
    # 정사각형의 둘레 계산
    perimeter = 4 * side_length
    
    # 넓이와 둘레를 튜플로 묶어서 반환
    return (area, perimeter)

# 예시 사용법
side_length = 5  # 예를 들어, 한 변의 길이가 5인 정사각형
result = square_properties(side_length)
print(f"정사각형의 넓이: {result[0]}, 둘레: {result[1]}")

# 하노이 탑 문제를 작성하라. (재귀함수 사용)
def hanoi_tower(n, start, target, auxiliary):
    """
    n개의 원판을 start에서 target으로 옮긴다.
    auxiliary는 보조 기둥으로 사용한다.

    Parameters:
    n (int): 옮길 원판의 수
    start (str): 시작 기둥
    target (str): 목표 기둥
    auxiliary (str): 보조 기둥
    """
    if n == 1:
        print(f"{start}에서 {target}로 원판 1을 옮김")
    else:
        # 1단계: n-1개의 원판을 시작 기둥에서 보조 기둥으로 옮긴다.
        hanoi_tower(n-1, start, auxiliary, target)
        # 2단계: 가장 큰 원판을 시작 기둥에서 목표 기둥으로 옮긴다.
        print(f"{start}에서 {target}로 원판 {n}을 옮김")
        # 3단계: n-1개의 원판을 보조 기둥에서 목표 기둥으로 옮긴다.
        hanoi_tower(n-1, auxiliary, target, start)

# 예시 사용: 3개의 원판을 'A' 기둥에서 'C' 기둥으로 옮기는 과정 출력하기
hanoi_tower(3, 'A', 'C', 'B')

# 재귀함수를 사용하여 n! 팩토리얼을 계산하는 함수를 작성하라.
def factorial(n):
    """
    n의 팩토리얼을 계산하는 재귀함수

    Parameters:
    n (int): 팩토리얼을 계산할 정수

    Returns:
    int: n의 팩토리얼 값
    """
    # 기본 경우: 0! = 1
    if n == 0:
        return 1
    # 재귀적으로 n! = n * (n-1)! 계산
    else:
        return n * factorial(n-1)

# 예시 사용
print(factorial(5))  # 5! = 120 출력

# 소수 n은 1과 자기 자신(n)을 제외하고 2부터 n-1 사이에 약수가 하나도 없는 수이다. 임의의 수가 소수인지 판별하는 방법을 생각해 보자.
def is_prime(n):
    """
    소수 판별 함수
    
    Parameters:
    n (int): 판별하고자 하는 수
    
    Returns:
    bool: n이 소수이면 True, 아니면 False
    """
    # 1과 0은 소수가 아님
    if n <= 1:
        return False
    # 2부터 sqrt(n)까지의 수로 나누어떨어지는지 확인
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 예제 사용
print(is_prime(11))  # True 출력
print(is_prime(4))   # False 출력

# 다음 각 함수를 구현하고 이를 시험하는 프로그램을 작성해 실행해 보라.
# 1. 두 개의 매개변수 n, m을 전달받아 m x n개의 * 상자를 출력하는 프로그램을 작성
import math

# 1. m x n 상자 출력
def print_box(m, n):
    for _ in range(m):
        print('*' * n)
        
# 2. 하나의 숫자를 전달받아 숫자의 자리 합을 구하는 함수를 작성. (예: 123 -> 1+2+3 = 6)
# 2. 숫자의 자리 합
def digit_sum(number):
    return sum(int(digit) for digit in str(number))

# 3. 두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성. 두 개의 문자열이 같은 경우 -1을 반환
# 3. 서로 다른 처음 위치 반환
def first_diff_position(str1, str2):
    min_length = min(len(str1), len(str2))
    for i in range(min_length):
        if str1[i] != str2[i]:
            return i
    if len(str1) == len(str2):
        return -1
    else:
        return min_length
    
# 4. 숫자를 전달받아 그 수의 약수를 반환하는 함수를 작성
# 4. 숫자의 약수 반환
def divisors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

# 5. 문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환하는 함수를 작성
# 5. 문자열에서 문자의 위치 찾기
def find_char_positions(string, char):
    return [i for i, c in enumerate(string) if c == char]

# 6. 원의 반지름을 주면 원의 넓이를 계산하는 함수
# 6. 원의 넓이 계산
def circle_area(radius):
    return math.pi * (radius ** 2)

# 7. 구의 반지름을 주면 구의 부피를 계산하는 함수 sphereVolume()
# 7. 구의 부피 계산
def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

# 8. 크지 않은 자연수 n을 매개변수로 받아 n!(팩토리얼)을 계산해 반환하는 함수
# 8. 팩토리얼 계산
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# 9. 두 개의 정수가 주어지면 두 수 중에서 더 큰 수를 찾아서 이것을 반환하는 함수
# 9. 두 수 중 더 큰 수 반환
def max_of_two(a, b):
    return a if a > b else b

# 10. 섭씨온도를 화씨온도로 변환하여 반환하는 함수
# 10. 섭씨를 화씨로 변환
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 11. 3장의 x^n을 계산하는 반복문 예제 프로그램(power.py)은 n이 양의 정수라는 제약사항이 있다. 이것을 확장해 n이 양, 음, 0일 경우에도 동작하는 함수를
# 만들고 이것을 시험 해보라.
# 11. x^n 계산 (n이 양수, 음수, 0인 경우)
def power(x, n):
    if n == 0:
        return 1
    elif n > 0:
        return x * power(x, n-1)
    else:
        return 1 / power(x, -n)
    
# 12. 자연수 n이 소수인지 판별하는 함수 isPrime(n)을 만들고 이를 이용해 1부터 500까지 모든 소수를 출력하는 프로그램
# 12. 소수 판별 및 1부터 500까지 소수 출력
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_up_to_500():
    for i in range(1, 501):
        if is_prime(i):
            print(i, end=' ')
    print()
    
# 13. 사각형의 가로와 세로가 주어지면 사각형의 넓이와 둘레를 튜플로 반환하는 함수를 만들고 이를 실행해 보라.
# 13. 사각형의 넓이와 둘레 계산
def rectangle_properties(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

# 예제 실행
print_box(3, 5) # 3x5 크기의 * 상자 출력
print(digit_sum(123)) # 숫자 123의 자리수 합 출력
print(first_diff_position("hello", "world")) # 'hello'와 'world'의 첫 번째 다른 위치 출력
print(divisors(28)) # 28의 약수 리스트 출력
print(find_char_positions("hello world", "o")) # 'hello world'에서 'o'의 위치 리스트 출력
print(circle_area(5)) # 반지름이 5인 원의 넓이 출력
print(sphere_volume(5)) # 반지름이 5인 구의 부피 출력
print(factorial(5)) # 5 팩토리얼 결과 출력
print(max_of_two(10, 20)) # 10과 20 중 더 큰 수 출력
print(celsius_to_fahrenheit(30)) # 섭씨 30도를 화씨로 변환하여 출력
print(power(2, -3)) # 2의 -3승 계산 결과 출력
print_primes_up_to_500() # 1부터 500까지의 소수 출력
print(rectangle_properties(5, 10)) # 가로 5, 세로 10인 사각형의 넓이와 둘레 출력