# 4. Create a class cal4 that will calculate square of a number.
#  Create setdata() method which has one parameters that contain number. Create display() method that will calculate sum.
# (Function should return value)


class cal4:

    def setdata(self):
        self.number = float(input("enter the number :"))

    def display(self):
        square =( self.number * self.number)
        return square
        
    

cls=cal4()
cls.setdata()
cls.display()
print("square :", cls.display())
