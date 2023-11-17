"""Write a python program which prompts the user to enter a file or directory name,
and display information about that file or directory. """

import os
import shutil
try:
    #response = input("Enter a file or directory path: ")
    response = "C:\\Users\\Netsanet\\Desktop\\Python\\basic_Py\\test.txt"
    with open(response, "r"):
        if os.path.exists(response):
            print("Basename: " + os.path.basename(response))
            print("Last modified time: " + str(os.path.getmtime(response)))
            print("File size: " + str(os.path.getsize(response)))
except FileExistsError:
    print("That location doesn't exist.")
except FileNotFoundError:
    print("That file was not found!")
