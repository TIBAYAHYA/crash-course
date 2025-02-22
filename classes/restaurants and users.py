#class related testing, this is a simple code that deals with already written 
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type): #restaurant's attributes
        #attribues assigning
        self.restaurant_name =restaurant_name
        self.cuisine_type = cuisine_type
 
 #restaurant's methods
    def describe(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The cuisine type is :{self.cuisine_type}\n")
        
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name}")
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
    # user method
    def describe(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old, his adress is {self.adress},and his favorite food is {self.favorite_food}")
    def greet(self):
        print(f"Greetings, {self.first_name} {self.last_name} , welcome to the coding enviroment!")
#users instance creating
mike = User("mike","tyson",30,"earth","your meat")
jackson = User("jack","son",50,"pluto","his own meat")

# users instance calling
mike.describe()
jackson.describe()
mike.greet()
jackson.greet()