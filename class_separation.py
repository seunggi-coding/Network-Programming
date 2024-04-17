# 클래스 분리
# 클래스 크기가 너무 커지면 두 개의 클래스로 분리하고 한 클래스의 객체를 다른 클래스의 속성으로 사용하면 하나로 된 
# 클래스와 같은 효과를 가지게 할 수 있다.

# Car 클래스 정의
class Car():
    # 생성자 메소드 정의
    def __init__(self, make, model, year):
        self.make = make  # 제조사
        self.model = model  # 모델명
        self.year = year  # 제조년도
        self.odometer_reading = 0  # 주행거리, 기본값은 0

    # 차량의 전체 이름을 반환하는 메소드
    def get_car_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()  # 제조년도, 제조사, 모델명을 조합하여 타이틀 형식으로 반환
    
# Car 클래스를 상속받는 ElectricCar 클래스 정의
class ElectricCar(Car):
    # 생성자 메소드 정의
    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # 상위 클래스의 생성자 호출로 make, model, year 초기화
        self.battery = Battery()  # ElectricCar 클래스는 Battery 인스턴스를 속성으로 가짐

# Battery 클래스 정의
class Battery():
    # 생성자 메소드 정의
    def __init__(self, battery_size=70):
        self.battery_size = battery_size  # 배터리 크기, 기본값은 70

    # 배터리 정보를 출력하는 메소드
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")  # 배터리 크기 정보 출력

# ElectricCar 인스턴스 생성
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_car_name())  # 차량 이름 출력
my_tesla.battery.describe_battery()  # 배터리 정보 출력
