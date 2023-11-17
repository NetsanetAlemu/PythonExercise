# rock, paper, scissors game

import random

print("\n\n\n========= Rock, Paper, and Scissors Game =========")

while True:

    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    print("Computer: " + computer)
    print("Player: " + player)

    if computer == "rock" and player == "paper":
        print("Congratulations! You won!")
    elif computer == "rock" and player == "scissors":
        print("You lose!")
    elif(computer == "paper" and player == "rock"):
        print("You lose!")
    elif(computer == "paper" and player == "scissors"):
        print("Congratulations! You won!")
    elif(computer == "scissors" and player == "rock"):
        print("Congratulations! You won!")
    elif(computer == "scissors" and player == "paper"):
        print("You lose!")
    elif(computer == player ):
        print("It's a tie!")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye!")




