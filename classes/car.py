#this code is an attempt to represent a car class
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 #  a defaulat value of the car mitrage
    # car describing function
    def namely_descriptive(self):  #this will return a long and very  descriptive name of the car
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name #returns a value that gets print in the calling, apparently thats more efficient, or at least makes you look like you know what you are doing (you dont)
    #function for reading the odometer value
    def read_odometer(self):
        print(f"This Car has {self.odometer} miles on It")
    #assiging function
    def update_odometer(self,milage):
        if milage > self.odometer:
            self.odometer = milage
        else :
            print("That is a lie")
 #incrementation function
    def increment_odometer(self,addition):
        if addition > 0:
            self.odometer += addition 
        else :
            print("Be Honest!")
my_car = Car("Audi","A4",2019)


# function calling I guess
print(my_car.namely_descriptive())

my_car.update_odometer(159)

my_car.read_odometer()

my_car.update_odometer(150)

my_car.read_odometer()
my_car.update_odometer(200)
my_car.read_odometer()
my_car.increment_odometer(35)
my_car.read_odometer()