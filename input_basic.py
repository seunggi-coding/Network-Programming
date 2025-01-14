# 사용자로부터 섭씨온도를 입력받아 화씨온도로 변환합니다.
# float() 함수를 사용하여 실수로 변환합니다.
celsius = float(input("섭씨온도를 입력해주세요: "))
fahrenheit = celsius * 9/5 + 32
print(f"섭씨 {celsius}도는 화씨로 변환하면 {fahrenheit:.2f}도입니다.")  # 계산된 화씨온도를 소수점 둘째 자리까지 출력합니다.


# 사용자로부터 이름을 입력받아 환영 메시지를 출력합니다.
name = input("당신의 이름을 입력해주세요: ")
print(f"안녕하세요, {name}님!")  # 사용자가 입력한 이름을 포함하여 환영 메시지를 출력합니다.

# 사용자로부터 두 숫자를 입력받아 그 합을 출력합니다.
# input()으로 받은 값은 문자열이므로, int() 함수를 사용하여 정수로 변환합니다.
num1 = int(input("첫 번째 숫자를 입력해주세요: "))
num2 = int(input("두 번째 숫자를 입력해주세요: "))
print(f"{num1} + {num2} = {num1 + num2}")  # 두 숫자의 합을 계산하여 출력합니다.

# 사용자로부터 세 과목의 점수를 입력받아 평균을 계산합니다.
# float() 함수를 사용하여 실수로 변환합니다.
kor = float(input("국어 점수를 입력해주세요: "))
math = float(input("수학 점수를 입력해주세요: "))
eng = float(input("영어 점수를 입력해주세요: "))
average = (kor + math + eng) / 3
print(f"세 과목의 평균 점수는 {average:.2f}점입니다.")  # 계산된 평균 점수를 소수점 둘째 자리까지 출력합니다.

# 사용자로부터 태어난 년도를 입력받아 나이를 계산합니다.
# 현재 년도는 2024년으로 가정합니다.
birth_year = int(input("당신이 태어난 년도를 입력해주세요: "))
age = 2024 - birth_year
print(f"당신은 현재 {age}살입니다.")  # 계산된 나이를 출력합니다.

# 사용자로부터 여러 값을 콤마로 구분하여 입력받아 리스트로 변환합니다.
# 입력받은 문자열을 split() 함수를 사용하여 콤마를 기준으로 분리하고, 리스트로 만듭니다.
items = input("콤마로 구분하여 여러 값을 입력해주세요: ").split(',')
print(f"입력받은 값들: {items}")  # 입력받은 값들을 리스트 형태로 출력합니다.
