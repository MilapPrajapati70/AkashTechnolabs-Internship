# Write a program with use of inheritance: Define a class publisher that stores the name of the title.
#  Derive two classes book and tape, which inherit publisher. 
#  Book class contains member data called page no and tape class contain time for playing. 
# Define functions in the appropriate classes to get and print the details

class publisher:

    def titlee(self):
        
    
        self.title = "7 habits of highly effective people"
        print(" book title is ", self.title)

class book(publisher):

    def memberdata(self):
        print("page no. of books are 786")

class tape(publisher):

    def time(self):
    
        print("the time of laying tap is 5hrs")
    
b = book()
b.titlee()
b.memberdata()
t=tape()
t.time()



