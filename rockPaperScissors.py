# rock, paper, scissors

import random

game = ['rock', 'paper', 'scissors']

player1 = random.choice(game)
player2 = random.choice(game)
print("Player 1: " + player1)
print("Player 2: " + player2)

if player1 == "rock" and player2 == "paper":
    print("Player 2 won")
elif player1 == "rock" and player2 == "scissors":
    print("Player 1 won")
elif(player1 == "paper" and player2 == "rock"):
    print("Player 1 won")
elif(player1 == "paper" and player2 == "scissors"):
    print("Player 2 won")
elif(player1 == "scissors" and player2 == "rock"):
    print("Player 2 won")
elif(player1 == "scissors" and player2 == "paper"):
    print("Player 1 won")
elif(player1 == player2 == "rock"):
    print("It's a tie!")
elif(player1 == player2 == "paper"):
    print("It's a tie!")
else:
    print("It's a tie!")
