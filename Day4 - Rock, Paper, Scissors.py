import random

print("Rock, Paper, Scissors")

user_score = 0
comp_score = 0

def AddComputerScore():
    global comp_score
    comp_score += 1

def AddUserScore():
    global user_score
    user_score += 1

while True:
    comp_choice = random.randint(0, 2)
    print(f"\nUser Score = {user_score}")
    print(f"Computer Score = {comp_score}\n")
    user_choice = int(input("Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissors, Any key to to exit: "))

    if user_choice <= 2:
        if comp_choice == 0: # Computer = Rock
            if user_choice == 2: # User = Scissors
                print("Computer = Rock. Computer wins")
                AddComputerScore()
            elif user_choice == 1: # User = Paper
                print("Computer = Rock. User wins")
                AddUserScore()
            else:
                print("User = Rock, Computer = Rock")
        elif comp_choice == 1: # Computer = Paper
            if user_choice == 0: # User = Rock
                print("Computer = Paper. Computer Wins")
                AddComputerScore()
            elif user_choice == 2: #User = Scissors
                print("Computer = Paper. User wins")
                AddUserScore()
            else:
                print("User = Paper, Computer = Paper")
        else: # Computer = Scissors
            if user_choice == 1: # User = Paper
                print("Computer = Scissor. Computer Wins")
                AddComputerScore()
            elif user_choice == 0:  # User = Scissors
                print("Computer = Scissors. User wins")
                AddUserScore()
            else:
                print("User = Scissors, Computer = Scissors")
    else:
        break
