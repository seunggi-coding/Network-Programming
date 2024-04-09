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