print("\n\n\n========================================")
print("============ Geography Quiz ============")

#-------------------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)

#-------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct (:")
        return 1
    else:
        print("Wrong ):")
        return 0

#-------------------------------------------
def display_score(correct_guesses, guesses):
    print("----------------------------------------")
    print("RESULTS")
    print("----------------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end = " ")
    print()
    print("Guesses: ", end = "")
    for i in guesses:
        print(i, end = " ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Score: " + str(score) + "%")
    print("----------------------------------------")

#-------------------------------------------
def play_again():
    response = input("Do you want to play again? (yes/no): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False

questions = {"What is the capital city of Ethiopia?: ": "A",
             "What is the longest river in the world?: ": "B", 
             "What is the biggest island in Africa?: ": "C", 
             "How many continents are there in Earth?: ": "D"}

options = [["A. Addiss Ababa", "B. Paris", "C. Seul", "D. Moscow"],
           ["A. Nile", "B. Amazon", "C. Mississipi", "D. Euphrates"],
           ["A. Iceland", "B. Comoros", "C. Madagascar", "D. Japan"],
           ["A. 5", "B. 4", "C. 6", "D. 7"]]

new_game()

while play_again():
    new_game()

print("Bye!")

