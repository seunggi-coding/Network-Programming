# 임의의 정수가 짝수인지 홀수인지 판별하는 프로그램
# 1. 임의의 정수가 짝수인지 홀수인지 판별하는 프로그램
number = int(input("정수를 입력하세요: "))
# % 연산자를 이용해 2로 나눈 나머지가 0이면 짝수, 아니면 홀수입니다.
if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
    
# 이차방정식 ax^2 + bx + c = 0의 계수 a, b, c(a!=0)을 입력받아 판별식(D= b^2 - 4ac)을 이용해 근의 종류를 출력하는 프로그램
# 2. 이차방정식 ax^2 + bx + c = 0의 계수를 입력받아 판별식을 이용해 근의 종류를 출력하는 프로그램
a = float(input("a 값을 입력하세요 (a!=0): "))
b = float(input("b 값을 입력하세요: "))
c = float(input("c 값을 입력하세요: "))
# 판별식 D = b^2 - 4ac를 계산합니다.
D = b**2 - 4*a*c

# 판별식의 값에 따라 근의 종류를 판별합니다.
if D > 0:
    print("서로 다른 두 실근을 가집니다.")
elif D == 0:
    print("중근을 가집니다.")
else:
    print("허근을 가집니다.")
    
# 임의의 점수(0-100)를 입력받고 70미만이면 "불합격", 70이상이면 "합격", 80이상이면 "합격", "입학금면제 장학금", 90이상이면 "합격",
# "입학금면제 장학금", "등록금면제 장학금"을 출력하는 프로그램
score = int(input("점수(0-100)를 입력하세요: "))
# 점수에 따라 조건을 분기합니다.
if score >= 90:
    print("합격", "입학금면제 장학금", "등록금면제 장학금")
elif score >= 80:
    print("합격", "입학금면제 장학금")
elif score >= 70:
    print("합격")
else:
    print("불합격")
    
# 사용자로부터 cm 단위의 길이를 입력받는다. 입력값이 음수이면 "잘못 입력하였습니다."라는 메시지를 출력하고 양수이면 길이를 인치로 변환하여
# 출력하는 프로그램을 작성하라. (1인치 = 2.54cm)
# 4. cm 단위의 길이를 입력받아 인치로 변환하여 출력하는 프로그램
length_cm = float(input("길이(cm)를 입력하세요: "))
# 입력값이 음수인지 확인합니다.
if length_cm < 0:
    print("잘못 입력하였습니다.")
else:
    # 2.54cm를 1인치로 환산하여 변환합니다.
    length_inch = length_cm / 2.54
    print(f"{length_cm}cm는 {length_inch:.2f}인치입니다.")

# 1mile은 1.6km이다. 10 mile부터 200mile까지 10mile 간격으로 해당하는 mile이 몇 km인지 출력하는 프로그램을 작성하라.
# 1. 1mile은 1.6km이다. 10 mile부터 200mile까지 10mile 간격으로 해당하는 mile이 몇 km인지 출력
print("Mile to Kilometer Conversion:")
for mile in range(10, 201, 10):
    km = mile * 1.6
    print(f"{mile} mile = {km} km")
    
# 임의의 크지 않은 자연수 n을 입력받아 n!(팩토리얼)을 계산해 출력하는 프로그램을 반복문을 이용해 작성
n = int(input("\nEnter a small natural number for factorial calculation: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# 임의의 자연수 n이 입력되면 2부터 n까지의 모든 소수를 출력하는 프로그램
# 3. 임의의 자연수 n이 입력되면 2부터 n까지의 모든 소수를 출력
n = int(input("\nEnter a natural number to find prime numbers up to n: "))
print("Prime numbers are:")
for num in range(2, n + 1):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num, end=" ")
print()

# 임의의 금액 n이 입력되면(단 n의 최소 단위는 1000원) 그 금액을 만족하는 모든 경우를 출력하는 프로그램(중첩 반복문 사용)의 작성. 지폐
# (50000, 10000, 5000, 1000원권)만 사용함.
# 4. 임의의 금액 n이 입력되면 그 금액을 만족하는 모든 경우를 출력
n = int(input("\nEnter an amount (min 1000): "))
print("Ways to make the amount using notes:")
for i in range(n // 50000 + 1):
    for j in range((n - 50000 * i) // 10000 + 1):
        for k in range((n - 50000 * i - 10000 * j) // 5000 + 1):
            for l in range((n - 50000 * i - 10000 * j - 5000 * k) // 1000 + 1):
                if 50000 * i + 10000 * j + 5000 * k + 1000 * l == n:
                    print(f"50000원: {i}, 10000원: {j}, 5000원: {k}, 1000원: {l}")
                    
# 아스키 코드표를 출력하는 프로그램(아스키 값 32-126까지 출력)
# 5. 아스키 코드표를 출력 (아스키 값 32-126까지 출력)
print("\nASCII Table (32-126):")
for i in range(32, 127):
    print(f"{i} : {chr(i)}", end="  ")
print()

# 산술연산자를 사용해 임의의 소문자는 대문자로, 대문자를 소문자로 변환해 출력하는 프로그램
# 6. 산술연산자를 사용해 소문자는 대문자로, 대문자를 소문자로 변환
char = input("\nEnter a character to change case: ")
if 'a' <= char <= 'z':
    # Convert to uppercase
    print("Converted to uppercase:", char.upper())
elif 'A' <= char <= 'Z':
    # Convert to lowercase
    print("Converted to lowercase:", char.lower())
else:
    print("Please enter an alphabetic character.")
    
# 비트연산자를 사용해 임의의 소문자는 대문자로, 대문자는 소문자로 변환해 출력하는 프로그램
# 7. 비트연산자를 사용해 소문자는 대문자로, 대문자는 소문자로 변환
char = input("\nEnter a character to change case using bitwise operation: ")
# Toggle the 6th bit to change the case
print("Converted case:", chr(ord(char) ^ 32))

# 임의의 자연수 k를 각각 왼쪽과 오른쪽으로 n번 시프트 하는 프로그램(n : 크지 않은 자연수)
# 8. 임의의 자연수 k를 각각 왼쪽과 오른쪽으로 n번 시프트
k = int(input("\nEnter a natural number k for bit shifting: "))
n = int(input("Enter the number of shifts n: "))
print(f"k << n: {k << n} (Left shift)")
print(f"k >> n: {k >> n} (Right shift)")

# 윤년계산 방법을 이용해 2000년부터 2500년까지 윤년인 해를 출력하는 프로그램
# 9. 윤년계산 방법을 이용해 2000년부터 2500년까지 윤년인 해를 출력
print("\nLeap years from 2000 to 2500:")
for year in range(2000, 2501):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, end=" ")
print()

# 두 수의 최대공약수는 두 수를 나누어떨어지는 가장 큰 수이다. 예를 들어 (16, 24)의 최대공약수는 8이다. 두 수를 입력받아 아래의 알고리즘에 의해
# 최대공약수를 구하는 프로그램을 작성하라.
# 큰 수를 작은 수로 나눈 나머지를 구하라.
# 큰 수를 작은 수로 대체하고 작은 수는 나머지로 대체하라.
# 작은 수가 0이 될 때까지 반복하라. 마지막 큰 수가 최대공약수이다.
# 사용자로부터 두 개의 수를 입력받습니다.
num1 = int(input("첫 번째 수를 입력하세요: "))
num2 = int(input("두 번째 수를 입력하세요: "))

# 입력받은 두 수 중에서 큰 수와 작은 수를 구분합니다.
# 이는 알고리즘의 첫 단계에서 큰 수를 작은 수로 나누기 위함입니다.
if num1 > num2:
    big = num1
    small = num2
else:
    big = num2
    small = num1

# 작은 수가 0이 될 때까지 반복합니다.
while small != 0:
    # 큰 수를 작은 수로 나눈 나머지를 구합니다.
    remainder = big % small

    # 큰 수를 작은 수로 대체하고, 작은 수는 나머지로 대체합니다.
    # 이 과정을 통해 점점 더 작은 나머지를 구하게 됩니다.
    big = small
    small = remainder

# 작은 수가 0이 되었을 때, 마지막 큰 수가 최대공약수가 됩니다.
# 이는 유클리드 호제법의 원리를 따릅니다.
print(f"최대공약수는 {big}입니다.")