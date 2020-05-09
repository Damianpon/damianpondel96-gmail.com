class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range
        self.__traveled_distance = 0
    def drive(self, distance):
        if distance + self.__traveled_distance <= self.max_range:
            self.__traveled_distance += distance
            return distance
        else:
            to_travel = self.max_range - self.__traveled_distance
            self.__traveled_distance = self.max_range
            return to_travel

    def charge(self):
        self.__traveled_distance = 0
class TestElectricCar:
    def test_init(self):
        car = ElectricCar(100)
        assert car
    def test_drive(self):
        car = ElectricCar(100)
        assert car.drive(70) == 70
        assert car.drive(50) == 30
    def test_drive_over_distance(self):
        car = ElectricCar(50)
        assert car.drive(80) == 50
        assert car.drive(10) == 0
    def test_charge(self):
        car = ElectricCar(50)
        assert car.drive(80) == 50
        assert car.drive(80) == 0
        car.charge()
        assert car.drive(80) == 50