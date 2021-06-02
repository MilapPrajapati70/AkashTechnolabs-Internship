#3. Create a class cal3 that will calculate simple interest. Create constructor method which has three parameters 
# .Create calInterest() method that will calculate Interest . Create display() method that will display Interest.


class cal3:
     def __init__(self):
         self.p= float(input("enter the principle :"))
         self.r= float(input("enter the rate :"))
         self.t=float(input("enter the time :")) 
    
     def callinterset(self):
        self.interset= (self.p * self.r * self.t)/100
    
     def display(self):
        print("the simple interst :", self.interset)

myc = cal3()
myc.callinterset()
myc.display()
