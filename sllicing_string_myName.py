# 문자열  “My name is Seung Gi Moon”에  대해  다음  물음에 답하는  코드를  작성하여라
# 문자열 정의
text = "My name is Seung Gi Moon"

# 문자열의 문자수를 출력
print(len(text))  # 출력: 23

# 문자열을 10번 반복한 문자열을 출력
print(text * 10)

# 문자열의 첫 번째 문자를 출력
print(text[0])  # 출력: M

# 문자열에서 처음 4문자를 출력
print(text[:4])  # 출력: My n

# 문자열에서 마지막 4문자를 출력
print(text[-4:])  # 출력: Moon

# 문자열의 문자를 거꾸로 출력
print(text[::-1])  # 출력: nooM iG gneuS si eman yM

# 문자열에서 첫 번째 문자와 마지막 문자를 제거한 문자열을 출력
print(text[1:-1])  # 출력: y name is Seung Gi Moo

# 문자를 모두 대문자로 변경하여 출력
print(text.upper())  # 출력: MY NAME IS SEUNG GI MOON

# 문자를 모두 소문자로 변경하여 출력
print(text.lower())  # 출력: my name is seung gi moon

# 문자열에서 'a'를 'e'로 대체하여 출력
print(text.replace('a', 'e'))  # 출력: My neme is Seung Gi Moon
