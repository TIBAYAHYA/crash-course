#librarys importation
import unittest

#selfmade
from name_function import get_formatted_name


#this class is intended to test the name function
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self): #MUST START WITH test_ FOR IT TO AUTOMATICLY RUN WHEN WE CALL IT
        formated_name = get_formatted_name("michael","jackson")
        self.assertEqual(formated_name,"Michael Jackson")
    def test_first_last_middle_name(self): #MUST START WITH test_ FOR IT TO AUTOMATICLY RUN WHEN WE CALL IT
        formated_name = get_formatted_name("jeffry","epstein","the brilliant")
        self.assertEqual(formated_name,"Jeffry The Brilliant Epstein")

if __name__ == "__main__":
    print(unittest.main())