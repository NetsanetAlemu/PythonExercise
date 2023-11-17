print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print( "{:^150}".format("Student Registration Form"))
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
id_list = name_list = gender_list = age_list = dept_list = cgpa_list = []
answer = "YES"
j = 0
while answer == "YES":
    stu_id = input("ID: ")
    id_list.append(stu_id)
    name = input("Name: ")
    name_list.append(name)
    gender = input("Gender: ")
    gender_list.append(gender)
    age = int(input("Age: "))
    age_list.append(age)
    dept = input("Department: ")
    dept_list.append(dept)
    cgpa = float(input("CGPA: "))
    cgpa_list.append(cgpa)
        
    answer = input("Do you want to add another student? (yes/no): ").upper()


stu = [id_list, name_list, gender_list, age_list, dept_list, cgpa_list]

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
title =("ID ", "Name ", "Gender  ", "Age ", "Department ", "CGPA ")
for i in title:
    print("{:30}".format(i), end = "")
print()
print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
for i in stu[j]:
    print("{:<30}".format(i), end = "")
    print()
    j += 1
# stu_r =("ID\t ", "Name\t ", "Gender\t ", "Age\t ", "Department\t ", "CGPA\t ")
        # stu_re = {stu_r[0]:stu[0][0]}
# if answer == "NO":
#     pass
# else:
#     print("Enter either yes or no, only!")

