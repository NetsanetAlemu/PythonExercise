print("===== Simple Calculator ======")

answer = "y"
while(answer == "y" or answer == "Y"):
    num1 = float(input("Enter a value: "))
    operator = input("Enter operator from +, -, *, /, %: ")
    num2 = float(input("Enter a value: "))
    if(operator == "+"):
        print("Sum: " + str(num1 + num2))
    elif(operator == "-"):
        print("Difference: " + str(num1 - num2))
    elif(operator == "*"):
        print("Product: " + str(num1 * num2))
    elif(operator == "/"):
        print("Quotient: " + str(num1 / num2))
    elif(operator == "%"):
        print("Modulo: " + str(num1 % num2))
    else:
        print("Enter appropriate operator.")
    print("Enter y or Y if you want to continue.") 
    answer = input("Do you want to continue?: ")



