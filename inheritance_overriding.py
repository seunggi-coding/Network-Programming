class People:
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name
    
    def introMe(self):
        print("Name : ", self.__name, "age :", str(self.__age))
    
class Student(People):
    def __init__(self, age=0, name=None, grade=None):
        super().__init__(age, name)
        self.__grade = grade

    def introMe(self):
        super().introMe()
        print("Grade :", self.__grade)

p1 = People(15, "Lee")
p1.introMe()

p2 = Student(18, "Kim", "B")
p2.introMe()