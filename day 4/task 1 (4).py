# 1. Create a class cal1 that will calculate sum of three numbers.
#  Create setdata() method which has three parameters that contain numbers. 
#  Create display() method that will calculate sum and display sum.


class myclass:


    def setdata(self,n1,n2,n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3
    

    def display(self):
        
        print(" ans is :" ,n1+n2+n3)
n1=int(input("entervalue of n1 :"))
n2=int(input("enter value of n2 :"))
n3= int(input("enter value of n3 :"))
myc = myclass()
myc.setdata()
myc.display()
        
        
