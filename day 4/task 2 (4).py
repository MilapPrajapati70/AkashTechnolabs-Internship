# 2.Create a class cal2 that will calculate area of a circle. 
# Create setdata() method that should take radius from the user. Create area() method that will calculate area .
#  Create display() method that will display area


class cal2:

    def setdata(self):
        self.r = float(input("enter the radius of circle :"))
        print (" the radius of circle is :",self.r)

    def area(self):
        self.carea= 3.14*self.r*self.r
    def display(self):
        print("area of circle is:" , self.carea)
myc = cal2()

myc.setdata()
myc.area()
myc.display()
