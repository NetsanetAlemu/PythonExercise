from arithmetic import Arithmetic

class Operations(Arithmetic):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        try:
            quotient =  self.num1 / self.num2
        except ZeroDivisionError:
            print("Can't divide by Zero!")
        else:
            return quotient
         
    def restart():
        response = input("\nRestart? (yes/no): ")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False
        

