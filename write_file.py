import os

path = "C:\\Users\\Netsanet\\Desktop\Python\\basic_Py_exercise\\test.txt"

try:
    with open (path, "a") as file:
        text = input("Enter a message: ")
        file.write(text)
except FileNotFoundError as e:
    print(e)
    print("The file isn't found!")