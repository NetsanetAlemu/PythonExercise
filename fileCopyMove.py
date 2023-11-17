import os
import shutil

source = "a\\test.txt"
destination = "C:\\Users\\Netsanet\\Desktop\\Python\\test.txt"

answer = input("Enter \'move\' to move and \'copy\' to copy the file: ")

if answer == 'copy':
    try:
        if os.path.exists(destination):
            print("There's already a file there!")
        else:
            shutil.copyfile(source, destination)

    except FileNotFoundError:
        print(source + " was not found!")
elif answer == 'move':
    try:
        if os.path.exists(destination):
            print("There is already a file there!")
        else:
            os.replace(source, destination)
    except FileNotFoundError:
        print(source + " was not found!")
