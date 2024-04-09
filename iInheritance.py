class People:
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name
    
    def introMe(self):
        print("Name : ", self.__name, "age :", str(self.__age))
    
class Teacher(People):
    def __init__(self, age=0, name=None, school=None):
        super().__init__(age, name)
        self.school = school

    def showSchool(self):
        print("My School is ", self.school)

p1 = People(15, "Lee")
p1.introMe()

p2 = Teacher(48, "Kim", "HighSchool")
p2.introMe()
p2.showSchool()