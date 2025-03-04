
import unittest,random
 #the random importation is to make sure the raise is still correctly represented regardless of value,
 #sure thing we dont just randint() the value of an employee raise

from employee_class import Employee #just importing the employee class

class EmployeeTest(unittest.TestCase):
    

    def setUp(self):
        self.annual_salary = 50000
        self.costume_raise = random.randint(0,1000) #the non default value raise
        
        self.employee = Employee("Mark","Cuban",self.annual_salary)
    
    # this function tests the funcionality of the raise function on employee class, given no costume value
    def test_give_default_raise(self):

        self.employee.give_raise() 
        self.assertEqual(self.employee.annual_salary,self.annual_salary+5000) 
        #comparing annual salary stored on the employee class with annual salary originaly sent to the class + default raise value
    
    #this function tests the functionality of the raise function on employee class, given a costume value
    def test_give_costume_raise(self):
        self.employee.give_raise(self.costume_raise)
        self.assertEqual(self.employee.annual_salary,self.annual_salary+self.costume_raise)
        #comparing annual salary stored on the employee class with annual salary originally sent to the class + whatever was randomized as raise value
if __name__ == '__main__':
    unittest.main()