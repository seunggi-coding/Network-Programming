# ZeroDivisionError 예외 처리
try:
    # 0으로 나누기 시도
    result = 10 / 0
except ZeroDivisionError:
    print("0으로 나누기 오류 발생!")  # "0으로 나누기 오류 발생!" 출력

# IndexError 예외 처리
try:
    my_list = [1, 2, 3]
    # 존재하지 않는 인덱스 접근 시도
    print(my_list[3])
except IndexError:
    print("인덱스 범위를 벗어났습니다!")  # "인덱스 범위를 벗어났습니다!" 출력

# FileNotFoundError 예외 처리
try:
    # 존재하지 않는 파일 열기 시도
    with open('nonexistent_file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다!")  # "파일을 찾을 수 없습니다!" 출력

# ValueError 예외 처리
try:
    # 정수가 아닌 문자열을 정수로 변환 시도
    number = int("not_a_number")
except ValueError:
    print("값 오류 발생!")  # "값 오류 발생!" 출력

# NameError 예외 처리
try:
    # 정의되지 않은 변수 사용 시도
    print(undefined_variable)
except NameError:
    print("정의되지 않은 변수를 사용하려고 했습니다!")  # "정의되지 않은 변수를 사용하려고 했습니다!" 출력

# TypeError 예외 처리
try:
    # 숫자에 문자열 덧셈 시도
    result = 10 + "5"
except TypeError:
    print("타입 오류 발생!")  # "타입 오류 발생!" 출력

# 예외를 알 수 없는 경우
try:
    # 여기에 예외를 발생시킬 수 있는 코드 작성
    # 예를 들어, "1" + 2
    result = "1" + 2
except Exception as e:
    print(f"예외 발생! 예외 정보: {e}")  # "예외 발생! 예외 정보: unsupported operand type(s) for +: 'str' and 'int'" 출력

# try-except-finally 예제
try:
    # 예외가 발생할 수 있는 코드
    result = "1" + 2
except TypeError:
    print("타입 오류 발생!")  # "타입 오류 발생!" 출력
finally:
    # 예외 발생 여부와 상관없이 항상 실행됨
    print("try-except 블록을 빠져나왔습니다.")  # "try-except 블록을 빠져나왔습니다." 출력
