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

 #making a child class known as electric car, based off the parent class known as car
class ElectricCar(Car):
    #initializing attributes of parent class
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        #initializing attributes 
        self.battery_capacity = 9000
    def describe_battery(self):
        #this function simply prints the battery capacity
        print(f"Th capacity of your electric car is {self.battery_capacity}")
my_tesla = ElectricCar("tesla","model s",2019)
print(my_tesla.namely_descriptive())
