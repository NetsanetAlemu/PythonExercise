import os

path = "C:\\Users\\Netsanet\\Desktop\\Python\\basic_py_exercise\\test.txt"

try:
    with open(path) as file:
        print(file.read())
except FileExistsError:
    print("File doesn't exist!l")
