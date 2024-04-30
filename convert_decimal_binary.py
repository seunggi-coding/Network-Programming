# 사용자로부터 10진수 입력 받음
decimal = int(input("10진수를 입력하세요: "))

# 2진수를 저장할 변수 초기화
binary = ''

# 10진수가 0이 될 때까지 반복
while decimal > 0:
    # 2로 나눈 나머지를 구하여 2진수의 가장 오른쪽에 추가
    remainder = decimal % 2
    binary = str(remainder) + binary
    # 10진수를 2로 나누어 업데이트
    decimal = decimal // 2

# 결과 출력
print("변환된 2진수: ", binary)
