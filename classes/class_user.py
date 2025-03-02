class User:
    def __init__(self,first_name,last_name,age,adress,favorite_food): #users attributes
        #attributes assigning
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.adress = adress
      
        self.favorite_food = favorite_food
        self.logging_attempts = 0    
    # user method
    def describe(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old, his adress is {self.adress},and his favorite food is {self.favorite_food}")
    def greet(self):
        print(f"Greetings, {self.first_name} {self.last_name} , welcome to the coding enviroment!")

    # incrementation of logging attempts
    def read_logging_attempts(self):    
        print(f"The total amount of logging attempts is: {self.logging_attempts}")
    def increment_loggings(self):
        self.logging_attempts += 1
    
    #reset the loggings counter
    def loggings_reset(self):
        self.logging_attempts = 0
    