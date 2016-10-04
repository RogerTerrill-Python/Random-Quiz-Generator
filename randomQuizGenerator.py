#!/usr/bin/env python3

import random

# quiz data. Keys are states and values are capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey':'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh','North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Generate 35 quiz files.
for quizNum in range(35):                                                                   # 35 is for the 35 different versions of the test
    #Create the quiz and answer key files.
    quizFile = open('capitalquiz%s.txt' % (quizNum +1), 'w')                                # Variable quizFile is the file name with num of quizNum + 1 with write
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')                 # Variable answerKeyFile is the key file with respective num with write permissions
    
    #Write out the header for the quiz.
    quizFile.write('Name:\n\n Date:\n\nPeriod:\n\n')                                        # Write to file the header
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))            # Add 20 spaces and the title with Form Number
    quizFile.write('\n\n')                                                                  # Add two new lines to add spaces
    
    #Shuffle the order of the states.
    states = list(capitals.keys())                                                          # Creates a list of the keys which are states
    random.shuffle(states)                                                                  # Randomizes the states list
    
    # Loop thorugh all 50 states, making a question for each.
    for questionNum in range(50):                                                           # Start Loop for 50 questions
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]                                       # Take the list of states and pass it into the capitals dictionary
        wrongAnswers = list(capitals.values())                                              # Take all the values of dictionary into wrongAnswer
        del wrongAnswers[wrongAnswers.index(correctAnswer)]                                 # Delete the correctAnswer by returning index number of where correctAnswer is
        wrongAnswers = random.sample(wrongAnswers, 3)                                       # Take a random sample of 3
        answerOptions = wrongAnswers + [correctAnswer]                                      # answerOptions = the list of wrongAnswers and make correct answer a list as well to add together
        random.shuffle(answerOptions)                                                       # Shuffle the answers
        
    # Write the question and answer options to the quiz
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum])) # Question number and state[i](key)
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))              # The expression 'ABCD'[i] at line treats the string 'ABCD' as an array and will evaluate to 'A','B', 'C',
                                                                                        # and then 'D' on each respective iteration through the loop.
        quizFile.write('\n')                                                            # Space with newline
        
        #Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)])) #Write number and the correct letter index, ie. 'ABCD'[0] = 'A'
quizFile.close()
answerKeyFile.close()