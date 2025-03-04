from survey import AnonymousSurvey

import unittest

#a class for testing the AnonymousSurvey class
class AnonymousSurveyTest(unittest.TestCase):

  # seems that the goal of setUp() method is to not have to write long/confusing lines of codes later on when we test the methodes
    def setUp(self):    #creates objects that will be used to test all the methods, main use of this is so we dont have to type alot of stuff when testing
        question = "What is your mother language? " # the question to ask
        self.my_survey = AnonymousSurvey(question) #storing the survey object with the question
        self.responses = ["French","English","Arabic","Russian","Mandarin","Japanese"] # a list of responses that can be used later


    
    #a test to see If a single response is stored properly
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.answers) # testing If parameter is in the answers list

    def test_store_three_answers(self):

        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.answers)


if __name__ == "__main__":
    unittest.main()


    