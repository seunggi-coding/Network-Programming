# Object 클래스

# People 클래스 정의
class People(object):
    # 생성자 메소드
    def __init__(self, age=0, name=None):
        # 인스턴스 변수 __age와 __name을 초기화합니다.
        # 이 변수들은 더블 언더스코어(__)로 시작하기 때문에, 클래스 외부에서 직접적으로 접근할 수 없는 '프라이빗' 변수입니다.
        self.__age = age
        self.__name = name

    # 객체를 문자열로 표현할 때 사용되는 매직 메소드
    # 이 클래스의 인스턴스를 print 함수로 출력할 때, 이 메소드가 반환하는 문자열이 출력됩니다.
    def __str__(self):
        # 인스턴스 변수 __name과 __age를 사용하여 문자열을 구성하고 반환합니다.
        return "info -- Name : " + self.__name + " / age : " + str(self.__age)
    
# People 클래스의 인스턴스 p1을 생성합니다. 초기화할 때 age를 29, name을 "John"으로 설정합니다.
p1 = People(29, "John")
# p1 인스턴스를 print 함수로 출력합니다. 이 때 __str__ 메소드가 호출되어 그 반환값이 출력됩니다.
print(p1)
