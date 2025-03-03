from survey import AnonymousSurvey

import unittest

#a class for testing the AnonymousSurvey class
class AnonymousSurveyTest(unittest.TestCase):
    
    #a test to see If a single response is stored properly
    def test_single_response(self):
        question = "What Is your Mother Language?"
        the_survey_object = AnonymousSurvey(question) #survey class object
        the_survey_object.store_response("English") #using function that stores response
        
        self.assertIn("English",the_survey_object.answers) # testing If parameter is in the answers list

    def test_store_three_resoibse(self):
        question = "What is your Mother Language"
        responses = ["English","Mandarin","Russian"]
        the_survey_object = AnonymousSurvey(question)
        for response in responses:
            the_survey_object.store_response(response)
        for response in responses:
            self.assertIn(response,the_survey_object.answers)


if __name__ == "__main__":
    unittest.main()