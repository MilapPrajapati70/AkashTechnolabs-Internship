# Create a arith class.
#  The class should have a parameterized constructor and methods to add, 
#  subtract and multiply two numbers and to return the answers


class arith:

    def __init__(self):
        self.n1=n1
        self.n2=n2
    

    def add(self):
        addition = self.n1 + self.n2
        print("addition of two number is :", addition )

    def sub(self):
        subsraction = self.n1 - self.n2
        print("substraction of two number is :", subsraction )

    def multi(self):
        multiply = self.n1 * self.n2
        print("multiply of two number is :", multiply)

n1 = float(input("enter the first numer:"))
n2 = float(input('enter the second number :'))

cls = arith()
cls.add()
cls.sub()
cls.multi()

    
