#class related testing, this is a simple code that deals with already written 
class restaurant:
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
my_restaurant = restaurant("marhaba","sea food")
his_restaurant = restaurant("makaram","chiken based")
their_restaurant = restaurant("welcome","fast food")

# instance calling
restaurant.describe(my_restaurant)
restaurant.describe(his_restaurant)
restaurant.describe(their_restaurant)


class user:
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
#users instance creating
mike = user("mike","tyson",30,"earth","your meat")
jackson = user("jack","son",50,"pluto","his own meat")

# users instance calling
user.describe(mike)
user.describe(jackson)