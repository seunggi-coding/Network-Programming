# 집합 생성
my_set = {1, 2, 3, 4, 5}
print("집합 생성: ", my_set) # 중복 없는 숫자의 집합 생성

# 빈 집합 생성
empty_set = set() # set() 함수를 사용하여 빈 집합 생성
print("빈 집합 생성: ", empty_set)

# 집합의 개수 확인
print("집합의 개수: ", len(my_set)) # len() 함수로 집합 내 요소의 개수를 확인

# 요소 추가
my_set.add(6) # add() 메서드를 사용하여 새로운 요소 추가
print("요소 추가 후: ", my_set)

# 요소 제거
my_set.remove(6) # remove() 메서드를 사용하여 요소 제거, 요소가 없으면 KeyError 발생
print("요소 제거 후: ", my_set)

# 안전하게 요소 제거하기 (요소가 없어도 에러가 발생하지 않음)
my_set.discard(5) # discard() 메서드를 사용하여 요소를 안전하게 제거, 없는 요소를 제거해도 에러 발생하지 않음
print("요소 안전 제거 후: ", my_set)

# 교집합
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("교집합: ", set_a & set_b) # & 연산자 또는 intersection() 메서드로 교집합 계산

# 합집합
print("합집합: ", set_a | set_b) # | 연산자 또는 union() 메서드로 합집합 계산

# 차집합
print("차집합: ", set_a - set_b) # - 연산자 또는 difference() 메서드로 차집합 계산

# 대칭 차집합 (두 집합 중 하나에만 있는 요소들의 집합)
print("대칭 차집합: ", set_a ^ set_b) # ^ 연산자 또는 symmetric_difference() 메서드로 대칭 차집합 계산

# 부분 집합 연산
subset_a = {1, 2}
print("subset_a가 set_a의 부분 집합인가?: ", subset_a.issubset(set_a)) # issubset() 메서드로 부분 집합 여부 확인

# 상위 집합 연산
print("set_a가 subset_a의 상위 집합인가?: ", set_a.issuperset(subset_a)) # issuperset() 메서드로 상위 집합 여부 확인

# issubset() 사용
print("issubset()을 사용한 부분 집합 확인: ", subset_a <= set_a) # <= 연산자로도 부분 집합 여부를 확인할 수 있음
