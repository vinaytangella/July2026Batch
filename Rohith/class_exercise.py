class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def speed(self, speed):
        print(f'The {self.name} {self.model} is running at a speed of {speed} km/h.')

    def mileage(self, mileage):
        print(f'The {self.name} {self.model} has a mileage of {mileage} km/l.')

c1_obj = Car('Toyota', 'Camry', 2020)
c2_obj = Car('Honda', 'Civic', 2019)

c1_obj.speed(60)
c1_obj.mileage(25)
        