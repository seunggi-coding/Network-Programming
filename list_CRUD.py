# 연습문제 2
# 리스트 [1,2,3]에 대해 다음과 같은 처리를 하라.

list_a = [1,2,3]
print("초기 리스트: ", list_a)  # 초기 리스트: [1, 2, 3]

# 두 번째 요소를 17로 수정
list_a[1] = 17
print("두 번째 요소를 17로 수정: ", list_a)  # 두 번째 요소를 17로 수정: [1, 17, 3]

# 리스트에 4, 5, 6을 추가
list_a.append(4)
list_a.append(5)
list_a.append(6)
print("리스트에 4, 5, 6 추가: ", list_a)  # 리스트에 4, 5, 6 추가: [1, 17, 3, 4, 5, 6]

# 첫 번째 요소 제거
list_a.pop(0)
print("첫 번째 요소 제거: ", list_a)  # 첫 번째 요소 제거: [17, 3, 4, 5, 6]

# sort() 메서드와 sorted() 함수의 차이

# sort() 메서드는 리스트 자체를 정렬하며, 반환값은 None입니다. 즉, 원본 리스트가 변경됩니다.
# 예: list_a.sort()

# sorted() 함수는 정렬된 새로운 리스트를 반환합니다. 원본 리스트는 변경되지 않습니다.
# 예: sorted_list = sorted(list_a)

# 리스트를 요소 오름차순 정렬하기
list_a.sort()
print("오름차순 정렬: ", list_a)  # 오름차순 정렬: [3, 4, 5, 6, 17]

# 리스트를 요소 내림차순 정렬하기
list_a.sort(reverse=True)
print("내림차순 정렬: ", list_a)  # 내림차순 정렬: [17, 6, 5, 4, 3]

# 인덱스 3에 25 넣기
list_a.insert(3, 25)
print("인덱스 3에 25 추가: ", list_a)  # 인덱스 3에 25 추가: [17, 6, 5, 25, 4, 3]

# 인덱스 3의 값 빼기
list_a.pop(3)
print("인덱스 3의 값 제거: ", list_a)  # 인덱스 3의 값 제거: [17, 6, 5, 4, 3]

# 리스트를 오름차순으로 정렬된 새로운 리스트로 반환
sorted_list = sorted(list_a)
print("오름차순으로 정렬된 새 리스트: ", sorted_list)  # 오름차순으로 정렬된 새 리스트: [3, 4, 5, 6, 17]

# 리스트를 내림차순으로 정렬된 새로운 리스트로 반환
sorted_list_desc = sorted(list_a, reverse=True)
print("내림차순으로 정렬된 새 리스트: ", sorted_list_desc)  # 내림차순으로 정렬된 새 리스트: [17, 6, 5, 4, 3]

# 리스트 역순으로 출력
list_a.reverse()
print("리스트 역순으로 출력: ", list_a)  # 리스트 역순으로 출력: [3, 4, 5, 6, 17]

# 리스트 요소를 모두 제거
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("리스트 요소를 모두 제거 전: ", letters)  # 리스트 요소를 모두 제거 전: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[:] = []
print("리스트 요소를 모두 제거 후: ", letters)  # 리스트 요소를 모두 제거 후: []

# 리스트 요소 합, 최소값, 최대값 구하기
num = [1,2,3,4,5]
print("리스트 요소 합: ", sum(num))  # 리스트 요소 합: 15
print("리스트 요소 최소값: ", min(num))  # 리스트 요소 최소값: 1
print("리스트 요소 최대값: ", max(num))  # 리스트
