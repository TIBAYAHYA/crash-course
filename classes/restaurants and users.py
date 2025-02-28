#class related testing, this is a simple code that deals with already written 
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type): #restaurant's attributes
        #attribues assigning
        self.restaurant_name =restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
 
 #restaurant's methods
    def describe(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The cuisine type is :{self.cuisine_type}\n")
        
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name}")

    #served clients related functions

    # this function serves the simple purpose of printing the value of served clients
    def read_served_clients(self):
        print(f"A total of {self.number_served} clients have been served!")

    # this function assigns the served clients a fresh value
    def change_served_clients(self,to_change_value):
        self.number_served = to_change_value
    # increment the served clients value
    def increment_served_client(self,addition):
        self.number_served += addition



#instance creation
my_restaurant = Restaurant("marhaba","sea food")
his_restaurant = Restaurant("makaram","chiken based")
their_restaurant = Restaurant("welcome","fast food")



# instance calling
my_restaurant.describe()
his_restaurant.describe()
their_restaurant.describe()

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
    

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate","vanilla","caramel","goodFlavor"]
    def display_flavors(self):
        print(f"The current availalble flavors are: {", ".join(self.flavors)}")
 
    

class Privileges():
    def __init__(self,privileges):
        self.privileges = privileges



class Admin(User):
    def __init__(self, first_name, last_name, age, adress, favorite_food):
        super().__init__(first_name, last_name, age, adress, favorite_food)
        #the attribute below stores a list of privilages an admin is granted!
        self.privileges = Privileges(["can add post","can delete post","can ban user","can throw up","can sneeze"])
    def display_privileges(self):
        print(f"The set of privilages an administrator is granted are : {", ".join(self.privileges)}")

admin = Admin("jack","tyson",35,"earth","same as his brother")

#users instance creating
mike = User("mike","tyson",30,"earth","your meat")
jackson = User("jack","son",50,"pluto","his own meat")

my_iceCream = IceCreamStand("stand","glacial")
my_iceCream.display_flavors()
        

    

admin.privileges.display_privileges()




# users instance calling
    
mike.describe()
jackson.describe()
mike.greet()
jackson.greet()

my_restaurant.change_served_clients(3)
my_restaurant.read_served_clients()
my_restaurant.increment_served_client(50)
my_restaurant.increment_served_client(30)
my_restaurant.read_served_clients()


mike.increment_loggings()
mike.increment_loggings()
mike.increment_loggings()
mike.read_logging_attempts()
mike.loggings_reset()
mike.read_logging_attempts()