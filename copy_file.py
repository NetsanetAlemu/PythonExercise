# copying data from one file to another

import shutil
import os

source = "C:\\Users\\Netsanet\\Documents\\NP\\Summer Project\\Tasks.txt"
destination = "C:\\Users\\Netsanet\\Desktop\\Python\\basic_py_exercise\\test.txt"

try:
    with open(destination) as file:
        if os.path.exists(destination):
            shutil.copyfile(source, destination)
            print("copy successful!")

except FileExistsError:
    print("File doesn't exist!")