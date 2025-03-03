from survey import AnonymousSurvey

question = "What Is your Mother Language? "

#creating the AnonymousSurvey class object
the_survey = AnonymousSurvey(question=question) #dont get confused, original parameter naming and variable naming are just the same



while True:
    print(f"{question} (or q to quit)")
    live_answer = input()
    if live_answer == "q":
        break

    the_survey.store_response(live_answer) #storing te he response in a list hiden on another file

#showing the results of the survey
the_survey.show_results()

