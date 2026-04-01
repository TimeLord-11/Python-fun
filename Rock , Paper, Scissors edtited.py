import random

options = ["rock","paper","scissors"]  # using tupple () is better here but i want to practice with lists
playing = True

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
        #edited by Box -create added validation
        if player not in options:
            print("Invalid input! Please enter rock, paper, or scissors.")
            
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
   #Edited by Box-create changed 
    #if not input("Play again? (y/n): ").lower() == "y":
        #playing = False
    #To include validation
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
   
