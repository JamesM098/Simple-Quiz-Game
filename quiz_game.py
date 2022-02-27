##############################
### Simple Python Quiz Game ##
### Created by James Meyer ###
###   February 26, 2022    ###
##############################


### Purpose :
###    Refreshing myself with Python.
###       - Python syntax
###       - Python Dictionaries
###       - Passing variables between Python Functions


import random

# Main Game code that will call all of the functions to initialize the
# and introduce the game as well as play the game
def game():
    score = 0
    user = " "
    questionList ={}
    questionList = generateQuestions(questionList)

    user = intro(user)
    questions(user, score, questionList)



# Function to create the list of questions, as well as tying an answer to each question
# using a Python Dictionary format
def generateQuestions(mylist):
    mylist = {
        "What is 10 + 25? ": 35,
        "What year is it? ": 2022,
        "What does CPU stand for? ": "CENTRAL PROCESSING UNIT",
        "What is 100/10 ": 10,
        "How many seconds in a minute? ": 60,
        "What language am I writing this program in? ": "PYTHON",
    }
    return mylist


def questions(user, score, questionList):
    #Creating a flag to ask the user if they'd like to continue
    continue_flag = 1
    questions_asked = 0

    #Loop until the user is no longer interested
    while(continue_flag < 2):
        print(" **Question** ")
        questions_asked += 1
        
        #Grab a random question from the list of questions
        currentQuestion = random.choice(list(questionList))

        #Get the answer, and also conver it to an int if the answer is a number
        #or convert it to all uppercase to test against the answer in the dictionary
        if(isinstance(questionList[currentQuestion], int)):
            answer = int(input(currentQuestion))
        else:
            answer = input(currentQuestion).upper()
            
        #Test to see if the answer is correct for the current question - ask if they'd like to continue
        if(answer == questionList[currentQuestion]):
            #increment the score, display the score, and show the current score if users
            #answer is correct
            score+=1
            print("CORRECT!\nScore: ", score)
            continue_flag = askContinue(user, score, questions_asked)
        else:
            #otherwise, print that the user was incorrect and show their current score
            print(user + " INCORRECT!\nCurrent Score: ", score)
            continue_flag = askContinue(user, score, questions_asked)


#Function to ask the user if they'd like to continue playing or not
def askContinue(user, score, questions_asked):
    continue_flag = int(input(" Continue Playing?\n   1=yes  2=no\n "))
    if continue_flag == 1:
        print("\nCurrent Score: ", score)
    else:
        average_score = score/questions_asked*100
        print("\n"+user + " Final Score: ", score)
                                #this formats the average number to 2 decimal places
        print("Your average: ", '{:.2f}%'.format(average_score))
        exit()
    return continue_flag




# main driver code for the introduction that calls another function
# The 2nd function will return if the player is playing or not
def intro(user):
    interested =""

    #multiple return variables
    x, user=introduction(interested, user)
    # x is true (returned from other function)
    if(x):
        user=user.capitalize()
        print(user + " is going to play!")
        return user
    # x is not true
    else:
        print(user+ "...Exiting...")
        quit()


# returns if the user is playing or not
def introduction(interested, user):
    print("\n\n*** WELCOME TO THE QUIZ GAME ***\n")
    interested = input("Would you like to play? ").upper()
    print(interested)
    if(interested == "YES"):
        user=input("Enter your name: ")
        return True, user
    else:
        user = ""
        return False, user



# Main driver function
def main():
    game()

if __name__ == '__main__':
    main()