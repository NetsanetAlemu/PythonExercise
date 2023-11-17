def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ": ", value)

def a():
    uname = input("Enter your username: ")
    passw = input("Enter your password: ")
    return uname, passw
info = a()

display_info(User_name = info[0], Password = info[1])

print(sum(20, 39, 10, 40,100,1000))