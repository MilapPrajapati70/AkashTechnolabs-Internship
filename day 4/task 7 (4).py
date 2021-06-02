# Create a class cal6 that will calculate area of a square.
#  Create setdata() method that should take length from the user.
#  Create area() method that will calculate area . Create display() method that will display area .

class cal6:

    def setdata(self):
        length= float(input("enter the length of square :"))
        self.length=length
        
    def area(self):
        self.area = self.length*self.length

    def display(self):
        print("the area of square is:", self.area)

cls = cal6()
cls.setdata()
cls.area()
cls.display()
        
