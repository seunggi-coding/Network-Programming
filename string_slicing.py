# 문자열 슬라이싱(잘라내기)

# 문자열 정의
text = "Hello, World!"

# 전체 문자열 출력
print(text[:])  # 'Hello, World!'

# 문자열의 첫 번째 문자 출력
print(text[0])  # 'H'

# 문자열의 마지막 문자 출력
print(text[-1])  # '!'

# 첫 번째 문자부터 세 번째 문자까지 출력 ('Hel')
print(text[0:3])  # 'Hel'

# 시작 인덱스를 생략하고 5번째 문자까지 출력 ('Hello')
print(text[:5])  # 'Hello'

# 7번째 문자부터 마지막 문자까지 출력 ('World!')
print(text[7:])  # 'World!'

# 마지막 문자를 제외한 모든 문자 출력 ('Hello, World')
print(text[:-1])  # 'Hello, World'

# 문자열을 거꾸로 출력
print(text[::-1])  # '!dlroW ,olleH'

# 2개씩 건너뛰며 문자 출력 ('Hlo ol!')
print(text[::2])  # 'Hlo ol!'

# 문자열의 마지막 세 문자 출력 ('ld!')
print(text[-3:])  # 'ld!'

# 문자열의 뒤에서 세 번째 문자부터 뒤에서 첫 번째 문자까지 역순으로 출력 ('!dl')
print(text[-1:-4:-1])  # '!dl'

# 새로운 문자열 만드는 예제
# 'Hello'와 'World'를 슬라이싱하여 새로운 문자열 만들기
new_text = text[:5] + " " + text[7:-1]  # 'Hello World'
print(new_text)  # 'Hello World'

# 문자열 길이 확인 예제
# 문자열 'Hello, World!'의 길이 확인
length_of_text = len(text)
print(length_of_text)  # 13

# 문자열의 문자를 역순으로 만드는 예제
reversed_text = text[::-1]
print(reversed_text)  # '!dlroW ,olleH'

# 문자열의 문자를 역순으로 만드는 예제2
# 문자열 정의
text = "Hello, World!"

# 문자열을 역순으로 만들기 위한 빈 문자열 초기화
reversed_text = ""

# text 문자열의 길이만큼 반복하면서 마지막 문자부터 처음 문자까지 순회
for char in text:
    # 현재 문자를 새 문자열의 맨 앞에 추가
    reversed_text = char + reversed_text

# 역순으로 만든 문자열 출력
print(reversed_text)  # '!dlroW ,olleH'


# in/not in 연산자를 사용하여 문자열에서 문자를 조사하는 예제
# 'World'가 text 문자열에 포함되어 있는지 확인
print('World' in text)  # True

# 'Python'이 text 문자열에 포함되어 있지 않은지 확인
print('Python' not in text)  # True

#문자열 찾기 예제
# 문자열 정의
text = "Hello, World! Welcome to the Python world."

# count() 사용 예제
# 'o' 문자가 text 문자열에 몇 번 나타나는지 계산
o_count = text.count('o')
print(o_count)  # 출력: 4
# 'o' 문자가 4번 나타남

# find() 사용 예제
# 'World' 문자열이 text 문자열에서 처음으로 나타나는 위치(인덱스) 찾기
world_index = text.find('World')
print(world_index)  # 출력: 7
# 'World'는 인덱스 7에서 시작함

# rfind() 사용 예제
# 'o' 문자가 text 문자열에서 마지막으로 나타나는 위치(인덱스) 찾기
last_o_index = text.rfind('o')
print(last_o_index)  # 출력: 36
# 마지막 'o'는 인덱스 36에 위치함

# index() 사용 예제
# 'Welcome' 문자열이 text 문자열에서 처음으로 나타나는 위치(인덱스) 찾기
welcome_index = text.index('Welcome')
print(welcome_index)  # 출력: 14
# 'Welcome'은 인덱스 14에서 시작함

# 찾고자 하는 문자열이 없는 경우의 동작 비교
# find()는 찾고자 하는 문자열이 없으면 -1을 반환
not_found_find = text.find('Python3')
print(not_found_find)  # 출력: -1

# index()는 찾고자 하는 문자열이 없으면 ValueError 예외를 발생시킴
try:
    not_found_index = text.index('Python3')
    print(not_found_index)
except ValueError:
    print("문자열을 찾을 수 없습니다.")  # 출력: 문자열을 찾을 수 없습니다.

# 문자열 분리 예제
# 문자열 정의
text = "Hello, World! Welcome to the Python world."

# 공백을 기준으로 문자열 분리하기
words = text.split()
print(words)
# 출력: ['Hello,', 'World!', 'Welcome', 'to', 'the', 'Python', 'world.']
# 문자열이 공백을 기준으로 분리되어 리스트 형태로 반환됨

# 쉼표(,)를 기준으로 문자열 분리하기
phrases = text.split(',')
print(phrases)
# 출력: ['Hello', ' World! Welcome to the Python world.']
# 문자열이 쉼표(,)를 기준으로 분리되어 리스트 형태로 반환됨

# 마침표(.)를 기준으로 문자열 분리하기
sentences = text.split('.')
print(sentences)
# 출력: ['Hello, World! Welcome to the Python world', '']
# 문자열이 마침표(.)를 기준으로 분리되어 리스트 형태로 반환됨, 끝에 마침표가 있어서 마지막 요소는 빈 문자열임

# 최대 분리 횟수 지정하기 (최대 1번 분리)
limited_split = text.split(' ', 1)
print(limited_split)
# 출력: ['Hello,', 'World! Welcome to the Python world.']
# 공백을 기준으로 문자열을 최대 1번만 분리하여 두 부분으로 나눔

# 문자열에서 공백 제거하기 예제 :  strip(), rstrip(), lstrip()
text = "   Hello, World!   "
print(text.strip())  # 'Hello, World!'
print(text.lstrip())  # 'Hello, World!   '
print(text.rstrip())  # '   Hello, World!'

# 문자열 결합하기 : join()
words = ['Hello', 'World']
print(' '.join(words))  # 'Hello World'
print(', '.join(words))  # 'Hello, World'

# 문자열 채우기 : zfill()
number = "5"
print(number.zfill(3))  # '005'
