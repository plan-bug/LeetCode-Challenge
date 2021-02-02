class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.vehicle = [big, medium, small]
        

    def addCar(self, carType: int) -> bool:
        if (self.vehicle[carType-1]):
            self.vehicle[carType-1]-=1
            return True
        return False
        