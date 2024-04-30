# 사용자가 입력한 문자열에 대해 다음 물음에 답하라.
# 사용자로부터 문자열 입력 받기
user_input = input("문자열을 입력하세요: ")

# 1. 문자열의 문자 수를 출력
print("문자 수:", len(user_input))

# 2. 문자열을 10번 반복한 문자열 출력
print("10번 반복:", user_input * 10)

# 3. 문자열의 첫 번째 문자 출력
if len(user_input) > 0:
    print("첫 번째 문자:", user_input[0])
else:
    print("문자열이 비어있습니다.")

# 4. 문자열에서 처음 3문자 출력
print("처음 3문자:", user_input[:3])

# 5. 문자열에서 마지막 3문자 출력
print("마지막 3문자:", user_input[-3:])

# 6. 문자열을 거꾸로 출력
print("거꾸로:", user_input[::-1])

# 7. 문자열에 7번째 문자가 있으면 출력, 없으면 '문자가 없음' 출력
if len(user_input) >= 7:
    print("7번째 문자:", user_input[6])
else:
    print("문자가 없음")

# 8. 문자열에서 첫 번째 문자와 마지막 문자를 제거한 문자열 출력
if len(user_input) > 2:
    print("첫 번째와 마지막 문자 제거:", user_input[1:-1])
else:
    print("문자열이 너무 짧아 첫 번째와 마지막 문자를 제거할 수 없습니다.")

# 9. 문자열을 모두 대문자로 변경하여 출력
print("대문자로 변경:", user_input.upper())

# 10. 문자열을 모두 소문자로 변경하여 출력
print("소문자로 변경:", user_input.lower())

# 11. 문자열에서 'a'를 'e'로 대체하여 출력
print("'a'를 'e'로 대체:", user_input.replace('a', 'e'))

# 문자 'a'가 들어가는 단어를 키보드에서 입력받아 첫 번째 줄에는 'a'까지의 문자열을 출력하고 두 번째 줄에는 나머지 문자열을 출력하는 프로그램을 작성하라.
# Your word: happy
# ha / ppy
# 첫 번째 문제: 'a'가 들어가는 단어를 입력받아 'a'까지의 문자열과 나머지 문자열을 출력
# 사용자로부터 단어 입력 받기
word = input("Your word: ")

# 'a' 문자의 위치 찾기. find 메소드는 문자가 처음 나타나는 위치를 반환하며, 없으면 -1을 반환한다.
a_position = word.find('a')

# 'a'가 단어에 포함되어 있는 경우
if a_position != -1:
    # 문자 'a'까지의 문자열을 포함하여 출력
    print(word[:a_position+1], end=" / ")
    # 'a' 다음 문자부터 나머지 문자열 출력
    print(word[a_position+1:])
else:
    # 'a'가 없는 경우 메시지 출력
    print("The word does not contain 'a'.")
    
# 숫자를 문자열로 변화하는 방법은 str(num)을 이용한다. str(12) => '12'가 된다. 반대로 문자열을 숫자로 변환하려면 int(string)을 이용한다. 
# int('12') => 12가 된다. 이를 이용하여 1부터 1000까지의 숫자의 각 자리수의 합을 구하여 출력하는 프로그램을 작성하라. 예를 들어 234 => 2 + 3 + 4 = 9가 된다.
# 두 번째 문제: 1부터 1000까지의 숫자의 각 자리수의 합을 구하여 출력
# 1부터 1000까지 반복
for num in range(1, 1001):
    # 숫자를 문자열로 변환
    num_str = str(num)
    # 각 자리수의 합을 저장할 변수 초기화
    digit_sum = 0
    # 문자열로 변환된 숫자의 각 문자에 대해 반복
    for digit in num_str:
        # 문자를 숫자로 변환 후 합산
        digit_sum += int(digit)
    # 결과 출력
    print(f"{num} => {digit_sum}")
    
# 3명 이상 친구 이름 리스트를 작성하고 다음 내용을 프로그램에 추가하라.
# insert()로 맨 앞에 새로운 친구 추가
# insert()로 3번째 위치에 새로운 친구 추가
# append()로 마지막에 친구 추가
# 친구 이름 리스트를 생성합니다. 이미 3명의 친구가 리스트에 있습니다.
friends = ["James", "Robert", "Linda"]

# insert() 함수를 사용해 리스트의 맨 앞에 새로운 친구를 추가합니다.
friends.insert(0, "Tom")
# 이제 friends 리스트는 ["Tom", "James", "Robert", "Linda"]가 됩니다.

# insert() 함수를 사용해 리스트의 3번째 위치에 새로운 친구를 추가합니다. 인덱스는 0부터 시작하므로 3은 실제로 4번째 위치입니다.
friends.insert(2, "Alice")
# 이제 friends 리스트는 ["Tom", "James", "Alice", "Robert", "Linda"]가 됩니다.

# append() 함수를 사용해 리스트의 마지막에 새로운 친구를 추가합니다.
friends.append("Barbara")
# 이제 friends 리스트는 ["Tom", "James", "Alice", "Robert", "Linda", "Barbara"]가 됩니다.

# 리스트 [1, 2, 3]에 대해 다음 내용을 프로그램에 추가하라.
# 두 번째 요소를 17로 수정
# 리스트에 4, 5, 6을 추가
# 첫 번째 요소 제거
# 리스트를 요소 순서대로 배열하기
# 인덱스 3에 25 넣기
# 숫자 리스트를 생성합니다.
numbers = [1, 2, 3]

# 두 번째 요소를 17로 수정합니다. 인덱스는 0부터 시작하므로 두 번째 요소의 인덱스는 1입니다.
numbers[1] = 17
# 이제 numbers 리스트는 [1, 17, 3]이 됩니다.

# 리스트의 끝에 4, 5, 6을 추가합니다. 여러 개의 요소를 추가할 때는 extend() 함수를 사용할 수 있습니다.
numbers.extend([4, 5, 6])
# 이제 numbers 리스트는 [1, 17, 3, 4, 5, 6]이 됩니다.

# 첫 번째 요소를 제거합니다. 첫 번째 요소를 제거할 때는 del 키워드나 pop() 함수를 사용할 수 있습니다. 여기서는 del을 사용합니다.
del numbers[0]
# 이제 numbers 리스트는 [17, 3, 4, 5, 6]이 됩니다.

# 리스트를 요소의 순서대로 배열합니다. 이를 위해 sort() 함수를 사용합니다.
numbers.sort()
# 이제 numbers 리스트는 [3, 4, 5, 6, 17]이 됩니다.

# 인덱스 3의 위치에 25를 넣습니다. insert() 함수를 사용합니다.
numbers.insert(3, 25)
# 이제 numbers 리스트는 [3, 4, 5, 25, 6, 17]이 됩니다.

# 결과 출력
print("친구 목록:", friends)
print("숫자 목록:", numbers)

# for루프를 이용하여 다음과 같은 리스트를 생성하라.
# 0~49까지의 수로 구성되는 리스트
# 0~49까지의 수로 구성되는 리스트 생성
list1 = []
for i in range(50):  # 0부터 49까지 반복
    list1.append(i)  # 현재 숫자를 list1에 추가
    
# 1~50까지 수의 제곱으로 구성되는 리스트
# 1~50까지 수의 제곱으로 구성되는 리스트 생성
list2 = []
for i in range(1, 51):  # 1부터 50까지 반복
    list2.append(i**2)  # 현재 숫자의 제곱을 list2에 추가
    
# 크기가 같은 두 개의 리스트 L, M을 생성하고 두 리스트의 각 요소 합으로 구성되는 새로운 리스트를 생성하라. 예를 들어 L = [1, 2, 3], M = [4, 5, 6]이면
# 새로운 리스트는 [5, 7, 9]가 된다.
# 크기가 같은 두 개의 리스트 L, M을 생성하고 두 리스트의 각 요소 합으로 구성되는 새로운 리스트 생성
# 여기서 L은 list1, M은 list2로 가정
L = list1
M = list2
new_list = []  # 두 리스트의 각 요소 합을 저장할 새로운 리스트
for i in range(len(L)):  # L의 길이만큼 반복 (L과 M의 길이는 같다고 가정)
    new_list.append(L[i] + M[i])  # L과 M의 i번째 요소의 합을 new_list에 추가
    
# 사용자로부터 5개의 숫자를 문자열로 입력받아 각 숫자를 +로 연결한 문자열을 생성하라. 예를 들어 2, 5, 11, 33, 55를 입력하면
# '2+5+11+33+55'가 된다.
# 사용자로부터 5개의 숫자를 문자열로 입력받아 각 숫자를 +로 연결한 문자열 생성
numbers = input("5개의 숫자를 쉼표로 구분하여 입력하세요: ")  # 사용자 입력 받기
number_list = numbers.split(',')  # 입력받은 문자열을 쉼표 기준으로 분리하여 리스트로 변환
joined_string = '+'.join(number_list)  # 리스트의 요소들을 '+' 기호로 연결하여 문자열 생성

# 결과 출력
print("0~49까지의 수로 구성된 리스트:", list1)
print("1~50까지 수의 제곱으로 구성된 리스트:", list2)
print("L과 M의 각 요소 합으로 구성된 새로운 리스트:", new_list)
print("입력받은 숫자들을 +로 연결한 문자열:", joined_string)

# 다음 딕셔너리에 대해 물음에 답하라.
# days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 
# 'October': 31, 'November': 30, 'December': 31}
# 사용자가 월을 입력하면 해당 월에 일수를 출력하라
# 알파벳 순서로 모든 월을 출력하라
# 일수가 31인 월을 모두 출력하라
# 월의 일수를 기준으로 순서가 정해진 (key-value) 쌍을 출력하라.
# 사용자가 월을 3자리만 입력하면 월의 일수를 출력하라. (Jan, Feb 등)
# 주어진 딕셔너리
days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

# 1. 사용자가 월을 입력하면 해당 월에 일수를 출력
user_month = input("Enter a month: ")  # 사용자로부터 월 입력 받기
# 입력한 월의 앞 세 글자를 대문자로 변환하여 일치하는 월 찾기
user_month = user_month.capitalize()
if user_month in days:
    print(f"{user_month} has {days[user_month]} days.")
else:
    # 입력한 월이 딕셔너리에 없을 경우, 앞 3글자를 기준으로 일치하는 월 찾기
    for month in days:
        if month.startswith(user_month):
            print(f"{month} has {days[month]} days.")
            break
    else:
        print("Invalid month entered.")

# 2. 알파벳 순서로 모든 월을 출력
print("\nMonths in alphabetical order:")
for month in sorted(days.keys()):
    print(month)

# 3. 일수가 31인 월을 모두 출력
print("\nMonths with 31 days:")
for month, day in days.items():
    if day == 31:
        print(month)

# 4. 월의 일수를 기준으로 순서가 정해진 (key-value) 쌍을 출력
print("\nMonths sorted by the number of days:")
for month in sorted(days, key=days.get):
    print(f"{month}: {days[month]} days")

# 주의: 이 코드는 사용자가 월을 정확하게 입력하거나 올바른 3자리 약어를 입력하는 것을 가정합니다.
# 또한, 약어로 여러 월이 일치할 수 있는 경우, 첫 번째로 일치하는 월의 일수만 출력됩니다.

# 다음 딕셔너리에 대해 물음에 답하라.
# d = [{'name' : 'Kim', 'phone' : '567-1414', 'email' : 'Kim@daum.net'},
# {'name' : 'Lee', 'phone' : '234-5678', 'email' : 'Lee@naver.com'},
# {'name' : 'Lee', 'phone' : '555-9876', 'email' : '']
# 전화번호가 8로 끝나는 사용자 이름을 출력하라.
# 이메일이 없는 사용자 이름을 출력하라.
# 사용자 이름을 입력하면 전화번호와 이메일을 출력하라. 이름이 없으면 '이름이 없습니다.'라는 메시지를 출력하라.
# 주어진 사용자 정보 리스트
d = [{'name' : 'Kim', 'phone' : '567-1414', 'email' : 'Kim@daum.net'},
     {'name' : 'Lee', 'phone' : '234-5678', 'email' : 'Lee@naver.com'},
     {'name' : 'Lee', 'phone' : '555-9876', 'email' : ''}]

# 1. 전화번호가 8로 끝나는 사용자 이름 출력하기
print("전화번호가 8로 끝나는 사용자:")
for person in d:
    if person['phone'].endswith('8'):  # 전화번호가 '8'로 끝나는지 확인
        print(person['name'])
print()  # 줄바꿈을 위한 print

# 2. 이메일이 없는 사용자 이름 출력하기
print("이메일이 없는 사용자:")
for person in d:
    if not person['email']:  # 이메일이 비어있는지 확인
        print(person['name'])
print()

# 3. 사용자 이름을 입력받아 전화번호와 이메일 출력하기
user_input = input("사용자 이름을 입력하세요: ").strip()  # 사용자 입력 받기
found = False  # 사용자를 찾았는지 여부를 저장할 변수

for person in d:
    if person['name'] == user_input:  # 입력받은 이름과 일치하는지 확인
        print(f"전화번호: {person['phone']}, 이메일: {person['email'] if person['email'] else '이메일 없음'}")
        found = True  # 사용자를 찾았으므로 True로 설정
        break  # 첫 번째로 일치하는 사용자를 찾았으므로 반복문 종료

if not found:  # 일치하는 사용자를 찾지 못한 경우
    print("이름이 없습니다.")

# set()을 사용하여 로또 번호 생성 프로그램
# whitle 문을 사용하고, random 모듈 사용, continue, break 사용
import random

# 로또 번호를 저장할 set 생성
lotto_numbers = set()

while True:
    # 1부터 45 사이의 임의의 숫자를 생성
    number = random.randint(1, 45)
    
    # 생성된 숫자를 set에 추가
    lotto_numbers.add(number)
    
    # 로또 번호가 6개가 되면 while 문 종료
    if len(lotto_numbers) == 6:
        break

# 생성된 로또 번호 출력
print(sorted(lotto_numbers))

# 리스트를 이용해 두 3X3 행렬의 덧셈, 뺄셈을 계산하는 프로그램을 실행하라.
# 두 3X3 행렬의 예시
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

# 덧셈 결과를 저장할 리스트
sum_result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

# 뺄셈 결과를 저장할 리스트
sub_result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

# 덧셈과 뺄셈 계산
for i in range(3):  # 행을 순회
    for j in range(3):  # 열을 순회
        sum_result[i][j] = A[i][j] + B[i][j]
        sub_result[i][j] = A[i][j] - B[i][j]

print("덧셈 결과:", sum_result)
print("뺄셈 결과:", sub_result)

# 위 프로그램을 임의의 두 MXN 행렬의 덧셈, 뺄셈을 계산하는 프로그램으로 확장하라.
def matrix_addition_subtraction(A, B):
    # 가정: A와 B는 같은 크기의 행렬
    sum_result = []
    sub_result = []

    for i in range(len(A)):
        sum_row = []
        sub_row = []
        for j in range(len(A[0])):
            sum_row.append(A[i][j] + B[i][j])
            sub_row.append(A[i][j] - B[i][j])
        sum_result.append(sum_row)
        sub_result.append(sub_row)

    return sum_result, sub_result

# 행렬 A와 B의 크기 입력받기 (MXN)
M = int(input("행의 수 M을 입력하세요: "))
N = int(input("열의 수 N을 입력하세요: "))

# 행렬 A와 B 초기화
A = []
B = []
print("행렬 A의 원소를 입력하세요:")
for i in range(M):
    A.append(list(map(int, input().split())))

print("행렬 B의 원소를 입력하세요:")
for i in range(M):
    B.append(list(map(int, input().split())))

sum_result, sub_result = matrix_addition_subtraction(A, B)

print("덧셈 결과:", sum_result)
print("뺄셈 결과:", sub_result)


# 사각형의 가로와 세로가 주어지면 사각형의 넓이와 둘레를 계산해 패킹하는 프로그램을 작성하라.
def rectangle_area_perimeter(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

# 가로와 세로 길이 입력받기 
width = float(input("사각형의 가로 길이를 입력하세요: "))
height = float(input("사각형의 세로 길이를 입력하세요: "))

area, perimeter = rectangle_area_perimeter(width, height)

print(f"사각형의 넓이: {area}, 둘레: {perimeter}")
