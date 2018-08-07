# Create a Rock, Paper, Scissors Game
# Rules: rock crushes scissors, Paper covers rock, Scissors cut Paper

#import Random
import Random

#Define the Compyter Choice Function
def rps():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice_rock()
    elif computer_choice == 2:
        computer_choice_paper()
    else:
        computer_choice_scissors()

#Define Function when computer chooses rock
def computer_choice_rock():
    user_choice = raw_input("1 for rock, 2 for paper, 3 for scissors: ")
    if user_choice == "1":
        print "You Tie. You chose Rock and the computer chose Rock."
        try_again()
    if user_choice == "2":
        print "You Win. You chose Paper and the computer chose Rock."
        try_again()
        if user_choice == "3":
        print "You Lose. You chose Scissors and the computer chose Rock."
        try_again()
    else:
        print "Try again"
        computer_choice_rock()


# Define Function when computer chooses Paper

#Define Function when computer chooses rock
def computer_choice_rock():
    user_choice = raw_input("1 for rock, 2 for paper, 3 for scissors: ")
    if user_choice == "1":
        print "You Lose. You chose Rock and the computer chose paper."
        try_again()
    if user_choice == "2":
        print "You Tie. You chose Paper and the computer chose paper."
        try_again()
        if user_choice == "3":
        print "You Win. You chose Scissors and the computer chose paper."
        try_again()
    else:
        print "Try again"
        computer_choice_rock()

# Define Function when computer chooses Scissors

def computer_choice_rock():
    user_choice = raw_input("1 for rock, 2 for paper, 3 for scissors: ")
    if user_choice == "1":
        print "You Win. You chose Rock and the computer chose scissors."
        try_again()
    if user_choice == "2":
        print "You Lose. You chose Paper and the computer chose scissors."
        try_again()
        if user_choice == "3":
        print "You Tie. You chose Scissors and the computer chose scissors."
        try_again()
    else:
        print "Try again"
        computer_choice_rock()

# Define Try Again Function
def try_again():
    choice = raw_input("would you like to play again? y/n ")
    if choice == "y" or choice == "yes" or choice == "Y"
        rps()
    elif choice == "n":
        print "Thanks for playing"
        quit()
    else:
        print "Try again"
        try_again()

rps()