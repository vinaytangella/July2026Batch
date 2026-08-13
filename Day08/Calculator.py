""""
    add,multiply,subtract,divide
    and return the value
    make sure you are using constructor, instance methods, class methods, static methods, class variables, local variables
"""
class Calculator:

    Brand = "Casio"

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return num1+num2

    def Multiply(self):
            return self.num1 * self.num2

    def subtract(self):
            return self.num1 - self.num2

    def divide(self):
            if self.num2 == 0:
                print("cannot divide with zero")
            else:
                print(f'Divide of {num1} and {num2} is' )
                return self.num1 // self.num2

    @classmethod
    def classmethod(cls):
          return cls.Brand

    @staticmethod
    def staticmethod():
          print("Welcome to Calculator")

num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
cal1 = Calculator(num1,num2)
print("Addition of 2 numbers is: ", cal1.add())
print("Multiplication of 2 numbers is: ", cal1.Multiply())
print("Subtraction of 2 numbers is: ", cal1.subtract())
print("Divide of 2 numbers is: ", cal1.divide())
