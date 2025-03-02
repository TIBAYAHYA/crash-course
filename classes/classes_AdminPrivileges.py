from class_user import User



class Privileges():
    def __init__(self,privileges):
        self.privileges = privileges[:-2]
    
        







class Admin(User):
    def __init__(self, first_name, last_name, age, adress, favorite_food):
        super().__init__(first_name, last_name, age, adress, favorite_food)
        #the attribute below stores a list of privilages an admin is granted!
        self.privileges = Privileges(["can add post","can delete post","can ban user","can throw up","can sneeze"])
    def display_privileges(self):
        print(f"The set of privilages an administrator is granted are : {", ".join(self.privileges.privileges)}")



        

    




