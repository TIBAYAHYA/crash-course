import unittest
from city_functions import city_country

class CityCountryTest(unittest.TestCase): # a testing function for city_country function
    def test_city_country(self):
        #testing to see If the the code is working as Intended, without population
        cool_naming = city_country("santiago","chile") #defining what to be taken as parameter from the function
        self.assertEqual(cool_naming,"Santiago, Chile") #result of function calling with cool_naming should equal to second parameter
    
    #this function tests If code works with population
    def test_city_country_population(self):
        cool_naming = city_country("santiago","chile",1000000)
        self.assertEqual(cool_naming,"Santiago, Chile - 1000000")

if __name__ == "__main__":
    print(unittest.main())