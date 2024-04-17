# People이라는 클래스를 정의합니다.
class People:
    # 생성자(__init__)를 정의합니다. 이 생성자는 기본적으로 age와 name의 기본값을 받습니다.
    def __init__(self, age=0, name=None):
        # 비공개 속성 ( __ )으로 age와 name을 설정합니다.
        self.__age = age
        self.__name = name
    
    # introMe라는 메서드를 정의합니다. 이 메서드는 객체의 이름과 나이를 출력합니다.
    def introMe(self):
        print("Name : ", self.__name, "age :", str(self.__age))
    
# Student라는 클래스를 정의하는데, People 클래스를 상속받습니다.
class Student(People):
    # 생성자(__init__)를 정의합니다. 이 생성자는 People의 생성자에 추가로 grade의 기본값을 받습니다.
    def __init__(self, age=0, name=None, grade=None):
        # super() 함수를 사용하여 부모 클래스(People)의 생성자를 호출합니다.
        # 이때, age와 name을 People 생성자에 전달합니다.
        super().__init__(age, name)
        # 비공개 속성으로 grade를 설정합니다.
        self.__grade = grade

    # introMe라는 메서드를 오버라이딩(재정의)합니다.
    def introMe(self):
        # super() 함수를 사용하여 부모 클래스(People)의 introMe 메서드를 호출합니다.
        # 이를 통해 이름과 나이를 출력합니다.
        super().introMe()
        # 추가적으로 학생의 학년을 출력합니다.
        print("Grade :", self.__grade)

# People 클래스의 인스턴스를 생성합니다. 나이는 15, 이름은 "Lee"입니다.
p1 = People(15, "Lee")
# People 클래스의 introMe 메서드를 호출하여, 이름과 나이를 출력합니다.
p1.introMe()

# Student 클래스의 인스턴스를 생성합니다. 나이는 18, 이름은 "Kim", 학년은 "B"입니다.
p2 = Student(18, "Kim", "B")
# Student 클래스의 introMe 메서드를 호출하여, 이름, 나이, 학년을 출력합니다.
# 이때, 부모 클래스(People)의 introMe 메서드도 함께 호출되어 이름과 나이가 출력되고,
# 그 다음으로 학년이 출력됩니다.
p2.introMe()
