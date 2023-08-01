def stu_reg():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    grade = input("Enter your grade: ")
    stud = {"Name" : name, "Age" : age, "Gender" : gender, "Grade" : grade}
    for key, value in stud.items():
        print(key + ": ", value)

    


def mark():
    math = float(input("Enter your math results out of 100: "))
    physics = float(input("Enter your physics results out of 100: "))
    ict = float(input("Enter your ict results out of 100: "))
    english = float(input("Enter your english results out of 100: "))
    total = math + physics + ict + english
    average = total / 4
    stud = {"Math" : math, "Physics" : physics, "Gender" : ict, "Grade" : english, "Total":total, "Average":average}
    for key, value in stud.items():
        print(key + ": ", value)

stu_reg()
mark()