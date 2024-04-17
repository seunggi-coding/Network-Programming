# 연습문제1
# 3명 이상 친구 이름 리스트를 작성하고 다음 내용을 프로그램 하라.

friends = ['철수', '영희', '민수']
print("초기 친구 이름 리스트: ", friends)

friends.insert(0, '지민')
print("맨 앞에 추가 후:", friends)

friends.insert(2, '수지')
print("3번째 위치에 추가 후:", friends)

friends.append('현우')
print("마지막에 추가 후:", friends)

print("==========================================================================================")

# 연습문제 2
# 리스트 [1,2,3]에 대해 다음과 같은 처리를 하라.

list_a = [1,2,3]
print(list_a)

# 두 번째 요소를 17로 수정
list_a[1] = 17
print(list_a)

# 리스트에 4, 5, 6을 추가
list_a.append(4)
list_a.append(5)
list_a.append(6)
print(list_a)

# 첫 번째 요소 제거
list_a.pop(0)
print(list_a)

# 리스트를 요소 오름차순 정렬하기
list_a.sort()
print(list_a)

# 리스트를 요소 내림차순 정렬하기
list_a.sort(reverse=True)
print(list_a)

# 인덱스 3에 25 넣기
list_a.insert(3, 25)
print(list_a)

print("==========================================================================================")

# 연습문제 3
# 다음과 같은 게임 프로그램을 작성하라
# 플레이어가 처음에 $50을 가지고 있다. 동전을 한 번 던져서 앞면(1) 또는 뒷면(2)이 나온다. 맞추면 $9를 따고 틀리면 
# $10을 잃는다. 플레이어가 돈을 모두 잃거나 $100이 되면 게임이 종료된다.
# 동전을 던져서 나오는 수는 다음 문장을 이용하라.
# from random import randint
# coin = randint(1, 2)
from random import randint

def coin_toss_game():
    total_money = 50

    while 0 < total_money < 100:
        coin = randint(1, 2)
        guess = randint(1, 2)

        if coin == guess:
            total_money += 9
        else:
            total_money -= 10

        print(f"동전 결과: {coin}, 추측: {guess}, 현재 금액: ${total_money}")

    if total_money <= 0:
        print("플레이어의 돈이 모두 소진되었습니다. 게임 오버!")
    else:
        print("축하합니다! 플레이어가 목표 금액을 달성했습니다!")

coin_toss_game()

print("==========================================================================================")

# 연습문제 4
# 두 수의 최대 공약수는 두 수를 나누어 떨어지는 가장 큰 수이다. 
# 예를 들어 (16, 24)의 최대 공약수는 8이다. 두 수를 입력 받아 다음 알고리즘에 의해 최대 공약수를 구하는
# 프로그램을 작성하라.
# 큰 수를 작은 수로 나눈 나머지를 구하라
# 큰 수를 작은 수로 대체하고 작은 수는 나머지로 대체하라
# 작은 수가 0이 될 때까지 이 과정을 반복하라. 마지막 큰 수가 최대 공약수이다.

def gcd(a, b):
    larger = 0
    smaller = 10000
    if(a > b):
        larger = a
        smaller = b
    else:
        larger = b
        smaller = a

    while smaller > 0:
        remain_num = larger % smaller
        larger = smaller
        smaller = remain_num
    return larger

if __name__ == "__main__":
    res = gcd(16, 24)
    print(f"최대공약수: {res}")

print("==========================================================================================")

# 연습문제 5
# 문자 'a'가 들어가는 단어를 키보드에서 입력 받아 첫 번째 줄에는 'a'까지의 문자열을 출력하고 두 번째 줄에는
# 나머지 문자열을 출력하는 프로그램을 작성하라.

str = input("Your word: ")

a_index = str.find('a')+1

if a_index != -1:
    # 여기에 +1을 하는 이유는, 슬라이싱에서 끝 인덱스는 포함되지 않으므로, 'a'까지 포함된 부분을 얻기 위해서입니다.
    print(str[:a_index])

    print(str[a_index:])
else:
    print("입력한 단어에는 'a'가 포함되어 있지 않습니다.")

# 두 번째 방법
# 'a'를 기준으로 문자열을 나누고, 최대 1번만 나눕니다.
# 따라서 결과는 최대 2개의 요소를 가진 리스트가 됩니다.
# str.split('a', 1): 이 코드는 문자열 str을 'a'를 구분자로 사용하여 분리합니다. 두 번째 인자 1은 분리 작업을 최대 몇 번 수행할지를 지정합니다. 
# 여기서는 1번만 수행하므로, 'a'를 기준으로 첫 번째 발견된 위치에서 문자열이 두 부분으로 나누어집니다.
parts = str.split('a', 1)

if len(parts) == 1:
    # 'a'가 없는 경우
    print("입력한 단어에는 'a'가 포함되어 있지 않습니다.")
else:
    # 'a'가 포함된 경우, 첫 번째 부분 출력 시 'a'를 덧붙여줍니다.
    print(parts[0] + 'a')
    # 두 번째 부분이 있으면 출력합니다.
    if len(parts) > 1:
        print(parts[1])

print("==========================================================================================")

# 연습문제 6
# 숫자를 문자열로 변화하는 방법은 str(num)을 이용한다. str(12) -> '12'가 된다. 반대로 문자열을 숫자로 변환하려면
# int(string)을 이용한다. int('12') -> 12가 된다. 이를 이용하여 1부터 1000까지의 숫자의 각 자리수릐 합을 모두 구하라.
# 예를 들어 234 -> 2+3+4=9가 된다.

total_sum = 0
str_num = input("숫자로 이루어진 문자열을 입력하시오. >> ")
for digit in str_num:
    total_sum += int(digit)

print(total_sum)

print("==========================================================================================")

# 연습문제 7
# for 루프를 이용하여 다음과 같은 리스트를 생성하라

# 0~49까지의 수로 구성되는 리스트
list_a = []
for i in range(0, 50):
    list_a.append(i)
print(f"list_a : {list_a}")

# 0~ 49까지 수의 제곱으로 구성되는 리스트
list_b = []
for i in range(0, 50):
    list_b.append(i**2)
print(f"list_b : {list_b}")

# map과 람다를 사용해서 해보기
#  map 함수는 첫 번째 인자로 주어진 함수를 두 번째 인자로 주어진 반복 가능한(iterable) 객체의 각 요소에 적용하고, 그 결과를 map 객체로 반환합니다.
list_c = []
list_c = list(map(lambda x: x, range(50)))
print(f"list_c : {list_c}")

list_d = []
list_d = list(map(lambda x: x**2, range(50)))
print(f"list_d : {list_d}")

print("==========================================================================================")

# 연습문제 8
# 아래 내용에 대한 프로그램(1개)를 작성하라
# days = {'January':31, 'Feburary':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31,
# 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}
# 사용자가 월을 입력하면 해당 월에 일수를 출력하라.
# 알파벳 순서로 모든 월을 출력하라
# 일수가 31인 월을 모두 출력하라
# 월의 일수를 기준으로 오른차순으로 (key-value) 쌍을 출력하라.
# 사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)

# 월별 일수 딕셔너리
days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
        'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

# 사용자로부터 월 입력 받기
user_input = input("월을 입력하세요 (전체 이름 또는 3자리 약어): ")

# 사용자 입력에 따라 해당 월의 일수 출력
for month, day in days.items():
    # 사용자 입력(user_input)을 받아서, 첫 글자를 대문자로 변경합니다(title() 함수 사용).
    # 이후 해당 입력이 days 딕셔너리의 키(월) 혹은 키의 앞 3글자와 일치하는지 확인합니다.
    # 예를 들어, "January"나 "Jan" 모두 일치하는 것으로 간주합니다.
    if user_input.title() in [month, month[:3]]:
        # 일치하는 월이 있다면, 해당 월과 그 월의 일수를 출력합니다.
        print(f"{month}는 {day}일.")
        # 일치하는 월을 찾았으므로 for 루프를 중단합니다.
        break
else:
    # for 루프가 break에 의해 중단되지 않고 정상적으로 끝났다면, 
    # 즉 사용자가 잘못된 입력을 했다면, 잘못 입력했다는 메시지를 출력합니다.
    print("잘못 입력했습니다.")


# 알파벳 순서로 모든 월 출력
print("\n알파벳 순서로 모든 월:")
for month in sorted(days.keys()):
    print(month)

# 일수가 31인 모든 월 출력
print("\n일수가 31인 모든 월:")
for month, day in days.items():
    if day == 31:
        print(month)

# 월의 일수를 기준으로 오름차순으로 (key-value) 쌍 출력
# days.items()는 딕셔너리의 모든 항목을 (키, 값) 쌍의 형태로 반환합니다. 
# 이 때, 각 항목(쌍)은 x로 표현되며, x[0]은 키(월의 이름)를, x[1]은 값(월의 일수)을 나타냅니다.
print("\n월의 일수를 기준으로 오름차순으로 (key-value) 쌍:")
for month in sorted(days.items(), key=lambda x: x[1]):
    print(month)


print("==========================================================================================")

# 연습문제 9
# 아래 내용에 대한 프로그램(1개)를 작성하라
""" d = [
    {'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
    {'name':'Helga', 'phone': '555-1618', 'email':'helga@mail.net'},
    {'name':'Princess', 'phone': '555-3141', 'email':''},
    {'name':'LJ', 'phone': '555-2718', 'email':'lj@mail.net'},
] """
# 전화번호가 8로 끝나는 사용자 이름을 출력하라.
# 이메일이 없는 사용자 이름을 출력하라.
# 사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다'라는 메시지를 출력하라.

d = [
    {'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
    {'name':'Helga', 'phone': '555-1618', 'email':'helga@mail.net'},
    {'name':'Princess', 'phone': '555-3141', 'email':''},
    {'name':'LJ', 'phone': '555-2718', 'email':'lj@mail.net'},
]

# 전화번호가 8로 끝나는 사용자 이름 출력
print("전화번호가 8로 끝나는 사용자:")
for person in d:
    if person['phone'].endswith('8'):
        print(person['name'])

# 이메일이 없는 사용자 이름 출력
print("\n이메일이 없는 사용자:")
for person in d:
    if not person['email']:
        print(person['name'])

# 사용자 이름을 입력받아 전화번호와 이메일 출력
user_name = input("\n사용자 이름을 입력하세요: ")
for person in d:
    if person['name'] == user_name:
        # 이메일 출력 부분에서는 조건부 표현식을 사용합니다. person['email'] if person['email'] else '이메일 없음'은 만약 person['email']이 참이라면
        # (즉, 값이 존재하면) 그 값을 사용하고, 그렇지 않으면 '이메일 없음' 문자열을 사용합니다.
        print(f"전화번호: {person['phone']}, 이메일: {person['email'] if person['email'] else '이메일 없음'}")
        break
else:
    print("이름이 없습니다.")


print("==========================================================================================")

# 연습문제 10
# 다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여 딕셔너리로 반환하는 함수를 포함하는 프로그램을 작성하라.
# 예) 문자열 'led=on&motor=off&switch=off'이고 구분 문자가 '&', '='일 때 {'led':'on', 'motor':'off', 'switch':'off'}
# 반환

# parse_query_string 함수는 쿼리 문자열을 파싱하여 딕셔너리로 반환합니다.
# query_string: 파싱할 쿼리 문자열
# delimiter1: 첫 번째 구분 문자(기본값 '&')
# delimiter2: 두 번째 구분 문자(기본값 '=')
def parse_query_string(query_string, delimiter1='&', delimiter2='='):
    # 결과를 저장할 빈 딕셔너리를 초기화합니다.
    result = {}
    
    # 첫 번째 구분 문자(delimiter1, 기본값 '&')로 문자열을 분리하여 반복합니다.
    for p in query_string.split(delimiter1):
        # 두 번째 구분 문자(delimiter2, 기본값 '=')로 각 부분을 다시 분리하여
        # key와 value를 얻습니다.
        print("p = ", p)
        # 언패킹 사용
        key, value = p.split(delimiter2)
        # 얻은 key와 value를 딕셔너리에 추가합니다.
        result[key] = value
    
    # 완성된 딕셔너리를 반환합니다.
    return result

# 테스트할 쿼리 문자열
string = 'led=on&motor=off&switch=off'
# parse_query_string 함수를 호출하여 문자열을 파싱한 결과를 얻습니다.
parsed_result = parse_query_string(string)
# 파싱된 딕셔너리를 출력합니다.
print(parsed_result)



print("==========================================================================================")

# 연습문제 11
# 다음 Person 클래스를 상속 받는 Employee 클래스를 정의하라.
# Employee 클래스에 employeeID 속성을 추가하고 getID() 메소드를 정의하라. getID()메소드를 employeeID를 반환하는 메소드이다.
# 최종적으로 Employee 클래스를 이용하여 Employee("IoT", 65, 2018)로 생성된 객체의 이름, 나이, ID를 출력하는 프로그램을 작성하라.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        print(self.name)
    
    def getAge(self):
        print(self.age)

class Employee(Person):
    def __init__(self, name, age, ID):
        super().__init__(name, age)
        self.ID = ID

    def getID(self):
        print(self.ID)

employee = Employee("IoT", 65, 2018)

employee.getName()
employee.getAge()
employee.getID()