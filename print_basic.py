# "abc" 문자열을 3번 반복하여 출력합니다.
print("abc" * 3)  # 출력 결과: abcabcabc

# 변수 a와 b에 각각 10과 5를 할당합니다.
a = 10
b = 5
# 변수 a와 b의 값을 출력하되, 사이에 "**"를 분리자로 사용하여 출력합니다.
print(a, b, sep="**")  # 출력 결과: 10**5

# print() 함수의 다양한 사용 예제

# 기본적으로 print() 함수는 여러 값을 콤마로 구분하여 전달할 수 있으며, 각 값은 공백으로 구분되어 출력됩니다.
print("Hello", "World")  # 출력 결과: Hello World

# sep 파라미터를 사용하여 값들 사이의 분리자를 지정할 수 있습니다.
print("Hello", "World", sep="-")  # 출력 결과: Hello-World

# end 파라미터를 사용하여 출력의 끝에 올 문자열을 지정할 수 있습니다. 기본값은 '\n'입니다.
print("Hello", end=" ")
print("World")  # 출력 결과: Hello World

# format을 사용한 문자열 포맷팅
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# 출력 결과: My name is John and I am 30 years old.

# % 연산자를 사용한 문자열 포맷팅 (%s, %d, %f의 사용)
print("My name is %s and I am %d years old." % (name, age))
# 출력 결과: My name is John and I am 30 years old.

# %5d는 총 5칸을 사용하여 정수를 오른쪽 정렬하여 출력합니다.
number = 7
print("%5d" % number)  # 출력 결과: '    7'

# %4.2f는 총 너비가 4칸인 실수를 출력하되, 소수점 아래는 2자리만을 표시합니다.
# 필요한 경우 반올림 적용
pi = 3.14159
print("%4.2f" % pi)  # 출력 결과: 3.14

# f-string을 사용한 문자열 포맷팅
# 변수의 값을 직접 문자열 안에 삽입할 수 있습니다.
print(f"My name is {name} and I am {age} years old.")
# 출력 결과: My name is John and I am 30 years old.

# f-string을 사용하여 정렬과 포맷팅을 할 수 있습니다.
# 예를 들어, 정수를 오른쪽으로 정렬
print(f"{number:5d}")  # 출력 결과: '    7'

# 실수를 포매팅하여 출력
print(f"{pi:4.2f}")  # 출력 결과: 3.14

# 더 복잡한 표현식도 f-string 안에서 사용할 수 있습니다.
print(f"Half of {number} is {number / 2}")  # 출력 결과: Half of 7 is 3.5
