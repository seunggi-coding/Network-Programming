from class_car import Car

class electriceCar(Car):
    def __init__(self, color, speed, charge):
        super().__init__(color, speed)
        self.charge = charge

