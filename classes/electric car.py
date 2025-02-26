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
    # a function for filling the car's gas tank
    def fill_gas_tank(self):
        print("The gas tank is being fileld...")
 #making a child class known as electric car, based off the parent class known as car

class Battery:
    def __init__(self,battery_size=100):
        self.battery_size = battery_size
    def describe_battery(self):
        #describes the battery size
        print(f"Your battery size is {self.battery_size}")
    def ev_range(self):
        if self.battery_size == 100:
            range = 300
        elif self.battery_size == 150:
            range = 400
        print(f"This car has a range of {range}")

class ElectricCar(Car):
    #initializing attributes of parent class
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        #initializing attributes 
        self.battery_capacity = 9000
        self.battery = Battery()
    def describe_battery(self):
        #this function simply prints the battery capacity
        print(f"Th capacity of your electric car is {self.battery_capacity}")
    #method override example, EVs dont have a gas tank
    def fill_gas_tank(self):
       print("Teslas dont have gas tank")
     
my_tesla = ElectricCar("tesla","model s",2019)
print(my_tesla.namely_descriptive())
my_tesla.battery.describe_battery()
my_tesla.battery.ev_range()