import random

def rock_paper_Scissors():

    rock = int(0)
    paper = int(1)
    scissors = int(2)

    pick = [rock, paper, scissors]
    answer1 = random.choice(pick)
    print(answer1)

    chocie = int(input("what do you want to choose from 0 to 2"))

    if chocie == 0 and answer1 == 2:
        print("you win")
    elif answer1 > chocie:
        print("computer win")
    else:
        print("your match is draw")
    return