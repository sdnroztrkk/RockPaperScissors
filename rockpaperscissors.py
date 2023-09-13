import random

choices = ["ROCK", "PAPER", "SCISSORS"]
userscore = 0
computerscore = 0


while (userscore < 3 and computerscore < 3):
    computerschoice = random.choice(choices)
    userschoice = input("ROCK, PAPER, SCISSORS???").upper().strip()

    if userschoice not in choices:
        print("Invalid choice. Please choose ROCK, PAPER, or SCISSORS.")
        continue

    elif userschoice == computerschoice:
        print("TIE! TRY AGAIN.")

    elif userschoice == "PAPER":
        if computerschoice == "ROCK":
            print("You win!")
            userscore += 1
        elif computerschoice == "SCISSORS":
            print("Computer wins!")
            computerscore += 1
        else:
            print("ERROR")
        

    elif userschoice == "ROCK":
        if computerschoice == "SCISSORS":
            print("You win!")
            userscore += 1
        elif computerschoice == "PAPER":
            print("Computer wins!")
            computerscore += 1
        else:
            print("ERROR")
        

    elif userschoice == "SCISSORS":
        if computerschoice == "PAPER":
            print("You win!")
            userscore += 1
        elif computerschoice == "ROCK":
            print("Computer wins!")
            computerscore += 1
        else:
            print("ERROR")

if userscore > computerscore:
    print(f"YOU WIN!\nComputer = {computerscore}\nYou = {userscore}")
else:
    print(f"COMPUTER WINS!\nComputer = {computerscore}\nYou = {userscore}")
    
        







