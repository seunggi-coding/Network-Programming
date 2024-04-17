# 딕셔너리 생성
person = {'name': 'John', 'age': 30, 'city': 'New York'}
print("딕셔너리 생성:", person)
# {'name': 'John', 'age': 30, 'city': 'New York'}

# 딕셔너리 키로 정렬하여 출력
print("키로 정렬된 딕셔너리:")
for key in sorted(person):
    print(f"{key}: {person[key]}")
# age: 30
# city: New York
# name: John

# 딕셔너리 값을 기준으로 정렬하여 출력
print("값으로 정렬된 딕셔너리:")
for key in sorted(person, key=person.get):
    print(f"{key}: {person[key]}")
# age: 30
# name: John
# city: New York

# 딕셔너리에서 키-값 쌍 제거
removed_value = person.pop('city')
print(f"'city' 키와 해당 값 {removed_value} 제거 후 딕셔너리:", person)
# {'name': 'John', 'age': 30}

# 딕셔너리의 모든 내용을 지우기
person.clear()
print("딕셔너리의 모든 내용을 지운 후:", person)
# {}

# 중첩 딕셔너리 예제
family = {
    'John': {'age': 30, 'job': 'Developer'},
    'Jane': {'age': 28, 'job': 'Designer'}
}
print("중첩 딕셔너리를 이용한 데이터 구조:", family)
# 중첩 딕셔너리를 이용해 가족 구성원의 정보를 저장

# 딕셔너리 생성
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# 딕셔너리 반복 및 언패킹
print("딕셔너리 반복 및 언패킹:")
for key, value in person.items():
    print(f"{key}: {value}")
# 출력 예시:
# name: John
# age: 30
# city: New York
