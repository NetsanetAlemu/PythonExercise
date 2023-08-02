def factorial():
    factorial = 1
    number = int(input("Enter a number: "))
    for counter in range(1, number + 1):
        factorial *= counter
    print("Factorial of " + str(number) + " is " + str(factorial))

factorial()