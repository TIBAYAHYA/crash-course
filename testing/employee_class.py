#this class is supposed to represent employees, with their name and salary
class Employee:
    
    #initializing the attributes of an emplyee
    def __init__(self,first_name,last_name,annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    #a function that gives a raise to the salary, with default amount being 5000 if no arguments were given
    def give_raise(self,raise_amount =5000):
        self.annual_salary += raise_amount  
        