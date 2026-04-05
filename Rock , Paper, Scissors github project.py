import random

options = ["rock","paper","scissors"] 
playing = True

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f'Player: {player}')
    print(f'Computer : {computer}')

    if player == computer:
        print("Its a tie")
    elif player == "rock" and computer == "scissors":
        print("You Rock! haha get it!")
    elif player == "scissors" and computer == "paper":
        print("Yes!! cut them down a size!")
    elif player == "paper" and computer == "rock":
        print("This seems sus but aparently you win anyways!")
    else:
        print("You Lose")
   # changed these lines with help from partner 
   # if not input("Play again? (y/n): ").lower() == "y":
    #    playing = False
#print()
#print("Thanks for playing!")
#changed above lines with help from partner

#updated lines below
while True:
        again = input("Play again? (y/n): ").lower()
        if again == "y":
            break
        elif again == "n":
            playing = False
            break
        else:
            print("Invalid input! Please enter 'y' or 'n'.")
            
print()
print("Thanks for playing!")
   
