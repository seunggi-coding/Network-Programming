# 문자열 "My name is Moon Seung Gi"에 대해 아래의 물음에 답하는 코드 작성

string = "My name is Moon Seung Gi"

# 문자열의 문자 수 출력
print("문자열의 문자 수:", len(string))

# 문자열을 10번 반복하여 출력
print("문자열을 10번 반복:", string * 10)

# 문자열의 첫 번째 문자 출력
print("문자열의 첫 번째 문자:", string[0])

# 문자열에서 처음 4문자 출력
print("문자열에서 처음 4문자:", string[:4])

# 문자열에서 마지막 4문자 출력
print("문자열에서 마지막 4문자:", string[-4:])

# 문자열의 문자를 거꾸로 출력
print("문자열의 문자를 거꾸로 출력:", string[::-1])

# 문자열에서 첫 번째 문자와 마지막 문자를 제거한 문자열 출력
print("첫 번째 문자와 마지막 문자를 제거한 문자열:", string[1:-1])

# 문자를 모두 대문자로 변경하여 출력
print("문자를 모두 대문자로 변경:", string.upper())

# 문자를 모두 소문자로 변경하여 출력
print("문자를 모두 소문자로 변경:", string.lower())

# 문자열에서 'a'를 'e'로 대체하여 출력
print("문자열에서 'a'를 'e'로 대체:", string.replace('a', 'e'))
