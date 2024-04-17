# 사용자로부터 연도를 입력받음
year = int(input("Type a year:"))

# 윤년 판별 조건
# 1. 연도가 4로 나누어떨어지면서 100으로 나누어떨어지지 않는 경우
# 2. 연도가 400으로 나누어떨어지는 경우
if (year % 4 == 0 and year % 100 != 0) or (year % 400) == 0:
    print(year, "is leap year")  # 위의 조건 중 하나라도 만족하면 윤년
else:
    print(year, "is not leap year")  # 위의 조건을 모두 만족하지 않으면 평년

# 이 코드는 윤년을 판별하는 규칙을 기반으로 합니다.
# 윤년은 그레고리안 달력에서 보통 4년에 한 번씩 2월이 29일까지 있는 해를 말합니다.
# 하지만 모든 4년마다 하는 것이 아니라, 100으로 나누어떨어지는 해는 윤년에서 제외되지만,
# 400으로 나누어떨어지는 해는 다시 윤년으로 포함됩니다.
# 이러한 규칙은 그레고리안 달력의 정확성을 유지하기 위해 필요합니다.