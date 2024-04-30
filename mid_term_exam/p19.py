class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

class GraduateStudent(Student):
    def __init__(self, name, age, graduateID, major):
        super().__init__(name, age)
        self.graduateID = graduateID
        self.major = major
        
    def getGraduateID(self):
        return self.graduateID
    
    def getMajor(self):
        return self.major


student = GraduateStudent("Seung Gi Moon", 24, 2019, "Internet of Things")
print(f"Name: {student.getName()}")
print(f"Age: {student.getAge()}")
print(f"ID: {student.getGraduateID()}")
print(f"Major: {student.getMajor()}")