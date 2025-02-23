#this code is an attempt to represent a car class
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 #  a defaulat value of the car mitrage

    def namely_descriptive(self):  #this will return a long and very  descriptive name of the car
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name
    def read_odometer(self):
        print(f"This Car has {self.odometer} miles on It")


my_car = Car("Audi","A4",2019)

print(my_car.namely_descriptive())
my_car.odometer += 25
my_car.odometer += 25   
my_car.read_odometer()