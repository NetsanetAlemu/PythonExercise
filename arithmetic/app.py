from operations import Operations
def main():
            try:
                num1 = float(input("\nEnter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Enter numbers only!")
            else:
                operation = Operations(num1, num2)
                print("\nSum: " + str(operation.add()))
                print("Differnce: " + str(operation.subtract()))
                print("Product: " + str(operation.multiply()))
                if operation.divide() == None:
                        print()
                else: 
                        print("Quotient: " + str(operation.divide()) + "\n")

main()

while Operations.restart():
      main()

print("\nBye!\n")