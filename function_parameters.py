# 매개변수의 기본값 지정
def greet(name="World"):
    """기본값을 가진 매개변수 예제"""
    print(f"Hello, {name}!")
greet()  # 출력: Hello, World!
greet("Python")  # 출력: Hello, Python!

# 가변 매개변수 (튜플)
def sum_numbers(*args):
    """튜플을 이용한 가변 매개변수 예제"""
    return sum(args)
print(sum_numbers(1, 2, 3))  # 출력: 6

# 가변 매개변수 (딕셔너리)
def print_info(**kwargs):
    """딕셔너리를 이용한 가변 매개변수 예제"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Python", version=3.8)

# 키워드를 이용한 매개변수 전달
def person_info(name, age, city):
    """키워드를 이용한 매개변수 전달 예제"""
    print(f"{name} is {age} years old, from {city}")
person_info(age=30, name="John", city="New York")

# pass 키워드
def empty_function():
    """아직 구현하지 않은 함수를 위한 pass 키워드 사용 예제"""
    pass

# 람다 함수
square = lambda x: x ** 2
"""람다 함수를 이용한 간단한 함수 정의 예제"""
print(square(5))  # 출력: 25

# 재귀 함수
def factorial(n):
    """재귀 함수를 이용한 팩토리얼 계산 예제"""
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))  # 출력: 120

# any 함수
print(any([False, True, False]))  # 출력: True
# 여러 값 중 하나라도 True이면 True를 반환하는 any 함수 예제

# 숫자를 이진수, 8진수, 16진수로 변환
print(bin(10))  # 출력: 0b1010
print(oct(10))  # 출력: 0o12
print(hex(255))  # 출력: 0xff
# 숫자를 이진수, 8진수, 16진수로 변환하는 함수 예제

# chr 함수
print(chr(97))  # 출력: 'a'
# 유니코드 코드 포인트에 해당하는 문자를 반환하는 chr 함수 예제

# dir 함수
print(dir([]))  # [] 인스턴스의 모든 속성 및 메서드를 나열하는 dir 함수 예제

# enumerate 함수
for index, value in enumerate(["a", "b", "c"]):
    """리스트의 요소와 인덱스를 동시에 반환하는 enumerate 함수 예제"""
    print(index, value)  # 0 a, 1 b, 2 c

# eval 함수
print(eval("5 + 5"))  # 출력: 10
# 문자열로 표현된 Python 표현식을 평가하는 eval 함수 예제

# filter 함수
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
"""조건에 맞는 요소만 필터링하는 filter 함수 예제"""
print(even_numbers)  # 출력: [2, 4, 6]

# map 함수
squared_numbers = list(map(lambda x: x ** 2, numbers))
"""리스트의 각 요소에 함수를 적용하는 map 함수 예제"""
print(squared_numbers)  # 출력: [1, 4, 9, 16, 25, 36]

# ord 함수
print(ord('a'))  # 출력: 97
# 문자의 유니코드 코드 포인트를 반환하는 ord 함수 예제

# repr 함수
print(repr("Hello\nWorld"))  # 출력: 'Hello\nWorld'
# 문자열의 인쇄 가능한 표현을 반환하는 repr 함수 예제

# round 함수
print(round(3.14159, 2))  # 출력: 3.14
# 숫자를 반올림하는 round 함수 예제

# zip 함수
names = ["John", "Jane", "Doe"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    """두 리스트의 요소를 짝지어주는 zip 함수 예제"""
    print(f"{name} is {age} years old")
# zip 함수를 이용하여 여러 시퀀스의 요소를 짝지어줍니다.
