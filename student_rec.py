def welcome():
    print("============================================================================================")
    print("\t\t\t\t\t Welcome")
    print("============================================================================================")
    try:
        answer = int(input("Enter 1 to to register \nEnter 2 to read record from file: "))
        if answer == 1:
            register()
        elif answer == 2:
            read_file()
        else:
            print("Choose from 1 or 2!")
    except ValueError:
        print("Enter only numbers!")


def register():
        print("-------------------------")
        print("Student Registration Form")
        print("-------------------------")
        stu_id = input("ID: ")
        name = input("Name: ")
        gender = input("Gender: ")
        age = int(input("Age: "))
        dept = input("Department: ")
        cgpa = float(input("CGPA: "))

        com =("ID: ", "Name: ", "Gender: ", "Age: ", "Department: ", "CGPA: ")

        answer = input("Do you want to add another student? (yes/no): ").upper()
        if answer == "YES":
            register()
        elif answer == "NO":
            main_menu()
        else:
            print("Enter either yes or no, only!")


def read_file():
    pass
def main_menu():
    pass

welcome()