# 집합 생성
my_set = {1, 2, 3, 4, 5}
print("집합 생성: ", my_set)

# 빈 집합 생성
empty_set = set()
print("빈 집합 생성: ", empty_set)

# 집합의 개수 확인
print("집합의 개수: ", len(my_set))

# 요소 추가
my_set.add(6)
print("요소 추가 후: ", my_set)

# 요소 제거
my_set.remove(6) # 요소가 집합에 없는 경우 KeyError 발생
print("요소 제거 후: ", my_set)

# 안전하게 요소 제거하기 (요소가 없어도 에러가 발생하지 않음)
my_set.discard(5)
print("요소 안전 제거 후: ", my_set)

# 교집합
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("교집합: ", set_a & set_b) # 또는 set_a.intersection(set_b)

# 합집합
print("합집합: ", set_a | set_b) # 또는 set_a.union(set_b)

# 차집합
print("차집합: ", set_a - set_b) # 또는 set_a.difference(set_b)

# 대칭 차집합 (두 집합 중 하나에만 있는 요소들의 집합)
print("대칭 차집합: ", set_a ^ set_b) # 또는 set_a.symmetric_difference(set_b)

# 부분 집합 연산
subset_a = {1, 2}
print("subset_a가 set_a의 부분 집합인가?: ", subset_a.issubset(set_a))

# 상위 집합 연산
print("set_a가 subset_a의 상위 집합인가?: ", set_a.issuperset(subset_a))

# issubset() 사용
print("issubset()을 사용한 부분 집합 확인: ", subset_a <= set_a)
