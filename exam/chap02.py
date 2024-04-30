# 자동차의 연료 효율을 미국식에서(mile/gallon)에서 한국식(km/l)로 바꾸는 프로그램을 작성하라.
# (단, 1마일은 1.6km이고, 1갤런은 3.7854리터이다.) 마일 수와 갤런 수를 입력받는다.
# 문제 1: 자동차의 연료 효율을 미국식에서 한국식으로 바꾸는 프로그램
miles = float(input("마일 수를 입력하시오: "))
gallons = float(input("갤런 수를 입력하시오: "))
# 변환 공식: (마일/갤런) * (1.6km/1마일) * (1갤런/3.7854리터) = km/l
km_per_liter = (miles / gallons) * (1.6 / 3.7854)
print("한국식 연료 효율: {:.2f} km/l".format(km_per_liter))

# 산술연산자를 이용하여 임의의 주어진 초를 분으로 바꾸는 프로그램
# 문제 2: 주어진 초를 분으로 바꾸는 프로그램
seconds = int(input("초를 입력하시오: "))
minutes = seconds / 60
print("분: ", minutes)

# 임의의 주어진 분을 입력받고, 그분에 해당하는 날짜와 나머지 시간과 나머지 분을 출력하는 프로그램을 만들어라. (예: 1550분은 1일 1시간 50분)
total_minutes = int(input("분을 입력하시오: "))
days = total_minutes // (24 * 60)
hours = (total_minutes % (24 * 60)) // 60
minutes = (total_minutes % (24 * 60)) % 60
print("{}일 {}시간 {}분".format(days, hours, minutes))

# 500만원을 연이율 5%로 저금했을 때 1년 후의 원리금의 합계를 출력하는 프로그램
principal = 5000000  # 원금
interest_rate = 0.05  # 연이율
total_amount = principal * (1 + interest_rate)
print("1년 후의 원리금의 합계: {:.2f}원".format(total_amount))

# 임의의 exam, report 점수를 입력받아, exam 점수가 90점 이상이거나 report 점수가 90점 이상이면 A학점이라고 출력하는 프로그램
exam_score = int(input("시험 점수를 입력하시오: "))
report_score = int(input("리포트 점수를 입력하시오: "))
if exam_score >= 90 or report_score >= 90:
    print("A학점")
else:
    print("A학점이 아닙니다.")
    
# 1부터 n까지의 합은 n(n+1) / 2로 주어진다. 1부터 100까지의 합을 구하여 출력하는 프로그램을 작성하고 실행하라.
n = 100
sum_n = n * (n + 1) / 2
print("1부터 100까지의 합: ", sum_n)

# 판매자가 딸기와 포도를 판매하고 있다. 포도 한 알의 무게는 75g이고, 딸기 한 알의 무게는 113.5g이다. 사용자로부터 포도알의 개수와 딸기의 개수를 입력받아
# 총 무게를 계산하여 출력하는 프로그램을 작성하고 실행하라.
grape_count = int(input("포도알의 개수를 입력하시오: "))
strawberry_count = int(input("딸기의 개수를 입력하시오: "))
total_weight = grape_count * 75 + strawberry_count * 113.5
print("총 무게: {:.2f}g".format(total_weight))