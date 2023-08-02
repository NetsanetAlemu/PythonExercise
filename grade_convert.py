def stu_reg():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    grade = input("Enter your department: ")
    return name, age, gender, grade


def mark():
    database = float(input("Enter your database results out of 100: "))
    security = float(input("Enter your security results out of 100: "))
    design = float(input("Enter your design results out of 100: "))
    return database, security, design


def convert_grade():
    markk = mark()
    grade = []
    for result in markk:
        if result >= 90 and result <= 100:
            grade.append("A+")
        elif result >= 80 and result < 90:
           grade.append("A")
        elif result >= 70 and result < 80:
            grade.append("B")
        elif result >= 60 and result < 70:
            grade.append("C")  
        else:
            grade.append("F")
    return grade

def stu_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ": ", value)

info = stu_reg()
mark_info = convert_grade()

stu_info(name = info[0], age = info[1], gender = info[2], grade = info[3])

stu_info(database = info[0], security = info[1], design = info[2])


    