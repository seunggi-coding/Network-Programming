# Rectangle 클래스를 정의합니다.
class Rectangle:
    # 생성자 메소드입니다. 너비(width)와 높이(height)를 인자로 받습니다.
    def __init__(self, width, height):
        # 너비와 높이가 양수인지 확인합니다.
        if width > 0 and height > 0:
            # 너비와 높이가 양수인 경우, 해당 값을 객체의 속성으로 저장합니다.
            self._width = width
            self._height = height
        else:
            # 너비나 높이가 양수가 아닌 경우, 경고 메시지를 출력합니다.
            print("너비와 높이는 양수여야 합니다.")

    # 면적을 계산하는 메소드입니다.
    def area(self):
        # 너비와 높이의 곱을 반환합니다.
        return self._width * self._height

    # 둘레를 계산하는 메소드입니다.
    def perimeter(self):
        # 둘레를 계산하여 반환합니다. (너비 + 높이) * 2 의 공식을 사용합니다.
        return 2 * (self._width + self._height)

# Rectangle 클래스로부터 상속받아 Square 클래스를 정의합니다.
class Square(Rectangle):
    # 생성자 메소드입니다. 한 변의 길이(side_length)를 인자로 받습니다.
    def __init__(self, side_length):
        # 부모 클래스의 생성자를 호출하여, 너비와 높이를 모두 한 변의 길이로 설정합니다.
        super().__init__(side_length, side_length)
        

# 직사각형 인스턴스를 생성합니다. 너비는 5, 높이는 10입니다.
rectangle = Rectangle(5, 10)
# 직사각형의 너비를 출력합니다. 접근은 직접 속성에 접근하여 이루어집니다.
print("직사각형의 너비:", rectangle._width)
# 직사각형의 높이를 출력합니다.
print("직사각형의 높이:", rectangle._height)
# 직사각형의 면적을 계산하여 출력합니다.
print("직사각형의 면적:", rectangle.area())
# 직사각형의 둘레를 계산하여 출력합니다.
print("직사각형의 둘레:", rectangle.perimeter())

# 정사각형 인스턴스를 생성합니다. 한 변의 길이는 5입니다.
square = Square(5)
# 정사각형의 한 변의 길이를 출력합니다. 정사각형은 모든 변의 길이가 같으므로 너비를 출력합니다.
print("\n정사각형의 한 변의 길이:", square._width)
# 정사각형의 면적을 계산하여 출력합니다.
print("정사각형의 면적:", square.area())
# 정사각형의 둘레를 계산하여 출력합니다.
print("정사각형의 둘레:", square.perimeter())
