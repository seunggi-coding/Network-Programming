# math 모듈의 factiorial(), degrees(), radians() 함수의 사용법을 조사하라.
import math

# 5의 팩토리얼 계산
print(math.factorial(5))  # 출력: 120

# 파이 라디안을 도로 변환
print(math.degrees(math.pi))  # 출력: 180.0

# 180도를 라디안으로 변환
print(math.radians(180))  # 출력: 3.141592653589793

# 'c:\>pip freeze' 명령을 이용하면 컴퓨터에 설치된 서드 파티 모듈을 알 수 있다. 자신의 컴퓨터에 설치된 서드 파티 모듈을 확인하라.
# 컴퓨터에 설치된 서드 파티 모듈 확인 방법
# 컴퓨터에 설치된 서드 파티 모듈을 확인하기 위해서는 커맨드 라인이나 터미널에서 pip freeze 명령어를 사용할 수 있습니다. 
# 이 명령어는 현재 환경에 설치된 모든 Python 패키지와 그 버전을 리스트업합니다.

# math 모듈의 함수를 이용해 임의의 각도를 라디안으로, 임의의 라디안을 각도로 변환하는 프로그램을 작성하라.
import math

# 각도에서 라디안으로 변환
def degrees_to_radians(degrees):
    return math.radians(degrees)

# 라디안에서 각도로 변환
def radians_to_degrees(radians):
    return math.degrees(radians)

# 사용 예제
degrees = 180
radians = math.pi

print(f"{degrees}도는 {degrees_to_radians(degrees)} 라디안입니다.")
print(f"{radians} 라디안은 {radians_to_degrees(radians)}도입니다.")


# math 모듈의 함수를 이용하여 sin(30) + cos(30)의 값을 계산하라.
import math

# 30도를 라디안으로 변환
radians_30 = math.radians(30)

# sin(30도) + cos(30도) 계산
result = math.sin(radians_30) + math.cos(radians_30)
print(f"sin(30) + cos(30)의 값은: {result}")


# 명령어 라인에서 다음과 같이 실행할 때 주어진 숫자의 합을 출력하는 addNumber.py 프로그램을 작성하라.
# $ python addNumber.py 1 2 3
# $ python addNumber.py 1 2 3 4 5 6
import sys

# 명령어 라인 인자를 가져옵니다. 첫 번째 인자(프로그램 이름)는 제외합니다.
numbers = sys.argv[1:]

# 문자열 리스트를 정수 리스트로 변환
numbers = [int(number) for number in numbers]

# 숫자들의 합을 계산
total = sum(numbers)

print(f"주어진 숫자들의 합: {total}")
