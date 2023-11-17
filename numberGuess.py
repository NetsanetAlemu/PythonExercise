import random

print("======== Guess My Number ==========")
      
num = random.randint(1, 20)
guess = 0

while(guess != num):
    guess = int(input("Guess a number between 1 and 20: "))
    if guess > num:
        print("Too high!")
    elif guess < num:
        print("Too low!")

print("You are correct!")

