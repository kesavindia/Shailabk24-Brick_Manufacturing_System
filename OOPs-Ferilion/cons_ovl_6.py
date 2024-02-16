'''Implement a class Vehicle with a constructor that can be
initialized with either the vehicle's make, model, and year or just the make and model (year defaults to 2023).'''
class Vehicle:
    def __init__(self,make,model,year=2023):
        self.make = make
        self.model = model
        self.year = year
    def ride(self,speed):
        return speed
car = Vehicle('honda','city',2021)
bike = Vehicle('honda','passion')
print(car.make)
print(bike.year)
Bike_speed = bike.ride(100)
print(f"Bike speed is {Bike_speed}km/hr")