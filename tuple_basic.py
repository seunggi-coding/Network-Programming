# 튜플 생성 예시
my_tuple = (1, 2, 3, 4, 5)
print("원본 튜플:", my_tuple)

# 튜플의 특정 요소 접근 예시
print("튜플의 첫 번째 요소:", my_tuple[0])

# 튜플 슬라이싱 예시
print("튜플의 두 번째 요소부터 네 번째 요소까지:", my_tuple[1:4])

# 튜플의 길이(요소의 수) 확인
print("튜플의 길이:", len(my_tuple))

# 튜플을 이용한 다중 할당
a, b, c, d, e = my_tuple
print("튜플을 이용한 다중 할당 결과:", a, b, c, d, e)

# 튜플은 변경 불가능하므로 아래 코드는 오류를 발생시킵니다.
# my_tuple[0] = 100  # TypeError 발생

# 튜플의 덧셈 연산을 통한 결합
another_tuple = (6, 7, 8)
combined_tuple = my_tuple + another_tuple
print("두 튜플의 결합:", combined_tuple)

# 튜플과 for 루프를 이용한 요소 접근
for item in my_tuple:
    print("튜플의 요소:", item)

# 튜플에서 요소가 한 개인 경우
# 요소가 하나인 튜플을 생성할 때는 요소 뒤에 콤마(,)를 붙여야 합니다.
single_element_tuple = (1,)
print("요소가 하나인 튜플:", single_element_tuple)

# 빈 튜플 생성
empty_tuple = ()
print("빈 튜플:", empty_tuple)

# * 기호를 사용한 튜플의 반복 및 결합
repeated_tuple = my_tuple * 2  # my_tuple을 두 번 반복
print("튜플 반복하여 결합:", repeated_tuple)

# 튜플과 리스트의 상호 변환 예제

# 튜플을 리스트로 변환
my_tuple = (1, 2, 3, 4, 5)
tuple_to_list = list(my_tuple)
print("튜플을 리스트로 변환:", tuple_to_list)

# 리스트를 튜플로 변환
my_list = [1, 2, 3, 4, 5]
list_to_tuple = tuple(my_list)
print("리스트를 튜플로 변환:", list_to_tuple)

# 튜플 언패킹 예시
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print("튜플 언패킹 결과:", a, b, c)

# 튜플의 일부 요소만 언패킹하기
# '*' 연산자를 사용하여 여러 요소를 한 변수에 할당할 수 있습니다.
my_tuple = (1, 2, 3, 4, 5)
a, *b, c = my_tuple
print("튜플의 일부 요소만 언패킹한 결과:", a)  # 1
print("'*' 연산자로 언패킹한 요소들:", b)  # [2, 3, 4]
print("튜플의 마지막 요소:", c)  # 5

# 튜플 언패킹을 이용한 변수 값 교환
x = 5
y = 10
print("교환 전:", x, y)
# 튜플 언패킹을 이용하여 x와 y의 값을 교환
x, y = y, x
print("교환 후:", x, y)

# 함수에서 튜플 언패킹 사용하기
# 함수가 튜플을 반환하면, 이를 여러 변수에 직접 할당할 수 있습니다.
def min_max(numbers):
    return min(numbers), max(numbers)  # 최소값과 최대값을 튜플로 반환

numbers = [1, 2, 3, 4, 5]
min_val, max_val = min_max(numbers)
print("최소값과 최대값:", min_val, max_val)