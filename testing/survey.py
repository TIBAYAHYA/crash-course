#this class collects anonymous answers to a specific survey question
class AnonymousSurvey:

    #initiation of the class
    def __init__(self,question):
        self.question = question #stores the given question
        self.answers = [] #initiates a list to store answers

    #function that prints the survey's question
    def show_question(self):
        print(self.question)

    #stores a single response into the list
    def store_response(self,answering):
        self.answers.append(answering)
    
    #a function that iterates over every element in the answer and prints It
    def show_results(self):
        print("Surveying results: \n")
        for index,answer in enumerate(self.answers):
            print(f"{index+1}- {answer}")

#some code I wrote to see If program is working as intended, sure I could have used the unittest but 
#this seemed more reliable at the moment
"""
survey_object1 = AnonymousSurvey("what is your name?") # an object created to store answer and be a reliable object
response_test_list = ["Jeff","Adolf","Epstein","Oppenheimer","Jackripper","Gankhas"] #virtual list of answer
for response in response_test_list:
    survey_object1.store_response(response) # append the list of answers into the target list, process is hidden behind a function

survey_object1.show_question()
survey_object1.show_result()#"""