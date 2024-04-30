# 문자열 예제
text = "Hello World 123"
number = "2024"
letters = "Python"
mixed = "Python3"

# isdigit() - 문자열이 숫자로만 구성되어 있는지 확인합니다.
print(number.isdigit())  # True
# isalpha() - 문자열이 알파벳 문자로만 구성되어 있는지 확인합니다.
print(letters.isalpha())  # True
# isalnum() - 문자열이 알파벳 문자나 숫자로만 구성되어 있는지 확인합니다.
print(mixed.isalnum())  # True
# isupper() - 문자열의 모든 알파벳이 대문자인지 확인합니다.
print("HELLO".isupper())  # True
# islower() - 문자열의 모든 알파벳이 소문자인지 확인합니다.
print("world".islower())  # True
# isspace() - 문자열이 공백 문자로만 구성되어 있는지 확인합니다.
print("   ".isspace())  # True
# upper() - 문자열의 알파벳을 모두 대문자로 변환합니다.
print(text.upper())  # HELLO WORLD 123
# lower() - 문자열의 알파벳을 모두 소문자로 변환합니다.
print(text.lower())  # hello world 123
# swapcase() - 문자열의 대소문자를 서로 바꿉니다.
print(text.swapcase())  # hELLO wORLD 123
# title() - 문자열에서 각 단어의 첫 글자만 대문자로 변환합니다.
print(text.title())  # Hello World 123
# count() - 특정 문자 또는 문자열이 주어진 문자열에 몇 번 나타나는지 세어줍니다.
print(text.count('o'))  # 2
# find() - 주어진 문자열에서 하위 문자열이 처음 나타나는 위치를 찾습니다. 찾지 못하면 -1을 반환합니다.
print(text.find('World'))  # 6
# rfind() - 주어진 문자열에서 하위 문자열이 마지막으로 나타나는 위치를 찾습니다. 찾지 못하면 -1을 반환합니다.
print(text.rfind('o'))  # 7
# index() - find()와 유사하지만, 하위 문자열을 찾지 못하면 ValueError를 발생시킵니다.
print(text.index('World'))  # 6
# split() - 주어진 문자열을 지정된 구분자로 나누어 리스트로 반환합니다. 구분자를 지정하지 않으면 공백을 기준으로 나눕니다.
print(text.split())  # ['Hello', 'World', '123']
# strip() - 문자열의 앞뒤에서 지정한 문자들을 제거합니다. 문자를 지정하지 않으면 공백을 제거합니다.
print("   Hello World   ".strip())  # Hello World
# rstrip() - 문자열의 끝에서 지정한 문자들을 제거합니다.
print("Hello World   ".rstrip())  # Hello World
# lstrip() - 문자열의 시작에서 지정한 문자들을 제거합니다.
print("   Hello World".lstrip())  # Hello World
# join() - 주어진 문자열 리스트의 요소들을 연결하여 하나의 문자열로 만듭니다. 각 요소 사이에는 지정한 문자열이 들어갑니다.
print(", ".join(['apple', 'banana', 'cherry']))  # apple, banana, cherry
# zfill() - 문자열의 길이가 지정한 너비에 도달하도록 문자열의 시작 부분에 '0'을 추가합니다.
print(number.zfill(6))  # 002024