# 예외처리 예제 (try-except-else-finally 구문)

def divide_numbers(x, y):
    """
    두 숫자의 나눗셈을 수행하는 함수.
    x: 분자
    y: 분모
    """
    try:
        result = x / y
    except ZeroDivisionError:
        # 분모가 0일 때 ZeroDivisionError 처리
        print("Error: 0으로 나눌 수 없습니다.")
    except ValueError:
        # x나 y가 숫자가 아닌 경우 ValueError 처리
        print("Error: 유효하지 않은 값이 입력되었습니다. 숫자만 입력하세요.")
    else:
        # 예외가 발생하지 않았을 때 결과를 출력
        print(f"{x} / {y} = {result}")
    finally:
        # 예외 발생 여부와 상관없이 실행
        print("연산이 완료되었습니다.")

# 함수 테스트
divide_numbers(10, 2)  # 정상 동작
divide_numbers(10, 0)  # 0으로 나눔, ZeroDivisionError 처리
# divide_numbers(10, 'a')  # ValueError 처리, 하지만 이 코드는 타입 체크를 하지 않아 실제로는 TypeError가 발생

# 주의: 위의 코드에서 ValueError 예외 처리는 실제로 발생하지 않습니다.
# '10'과 'a'를 함수에 전달할 경우, TypeError가 발생하기 때문입니다.
# 따라서 이 예외 처리는 예제의 일부로만 제공되며, 실제로 유효한 숫자가 입력되었는지 확인하려면
# 입력 값을 int 또는 float로 변환하는 과정에서 ValueError를 처리하도록 코드를 수정해야 합니다.

# 임의의 파일에 글자를 기록하여 저장하는 프로그램을 작성하라.
# 파일에 글자 기록 및 저장
file_name = 'example.txt'  # 저장할 파일 이름 지정

# 파일을 쓰기 모드로 열기
with open(file_name, 'w') as file:
    while True:
        text = input("저장할 글자를 입력하세요 (종료하려면 '종료' 입력): ")
        if text == '종료':  # 사용자가 '종료' 입력 시 반복 종료
            break
        file.write(text + '\n')  # 입력받은 텍스트를 파일에 쓰고, 줄바꿈 추가
    print(f"'{file_name}' 파일에 저장이 완료되었습니다.")


# 임의의 주어진 텍스트 파일의 내용을 화면에 출력하는 프로그램을 작성하라.
# 파일 내용 화면에 출력
file_name = 'example.txt'  # 읽을 파일 이름 지정

# 파일을 읽기 모드로 열기
try:
    with open(file_name, 'r') as file:
        print(f"'{file_name}' 파일의 내용:")
        while True:
            line = file.readline()  # 파일에서 한 줄 읽기
            if not line:  # 더 이상 읽을 내용이 없으면 종료
                break
            print(line, end='')  # 읽은 줄 출력
except FileNotFoundError:
    print(f"'{file_name}' 파일을 찾을 수 없습니다.")
