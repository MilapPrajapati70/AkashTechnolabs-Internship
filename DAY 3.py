# DAY 3
#ex:1 = "Calculate average of 5 (N)numbers."
n = int(input("enter how many num :"))
total = 0
for i in range (0,n):
    number =int(input("enter value of numbers : "))
    total += number
avg= total/n
print(total)
print(avg)

#ex :2.	Check whether number is even or odd.
n = int(input("enter any num :"))
if (n%2)  == 0:
    print( n , "is even number")
else:
        print( n ," is odd number")

#ex: 3.	Take a year and check whether it is leap year or not
year = int(input("enter year :"))
if(year%4) == 0 :
    print(year , "is a leap year")

else:
    print(year , " is a not leap year")

#ex : 4 Take a number and check whether it is zero, positive or negative.
n1= int(input("enter any num :"))
if n1==0:
    print("n1 is zero")
elif n1>0:
    print("n1 is postive number")
else :
    print("n1 is negative number")

#ex : 5.Take 2 numbers and display greatest number. (Also check equal number condition)
n1= int(input("enter any num :"))
n2= int(input("enter any num :"))
if n1==n2 :
    print("both numbers are equal")
elif n1>n2 :
    print(n1," is greater ")
else :
    print( n2 ," is greater")

# ex : 6
# Python program to find the factorial of a number provided by the user.


num = int(input("Enter a number: "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

# ex : 7 	Write a program to swap 2 numbers using third variable.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print(" numbers before swaapping ", num1 , num2)
temp = num1
num1 = num2
num2 = temp
print( "numbers after swapping " , num1 , num2)

# ex :8.Take 2 numbers and find smallest number.

n1= int(input("enter any num :"))
n2= int(input("enter any num :"))
if n1==n2 :
    print("both numbers are equal")
elif n1>n2 :
    print(n2," is smallest")
else :
    print( n1 ," is smallest")

# ex :9.Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even.
n1= int(input("enter any num :"))

if( n1< 100):
    if (n1%2)  == 0:
         print( n1 , "is even number")
    else:
        print( n1 ," is odd number")
else:
    print("number is greater than 100, so you write number less than 100. ")

# ex : 10Take a number to print the square of a number if it is less than 
n1= int(input("enter any num :"))

if (n1<10 ):
   num = n1*n1
   print(num)
else:
    print("num is greater than 10")

# ex :11.	Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement .

n1= float(input("enter any num :"))
if n1 >= 0 :
    if n1 ==0 :
        print("zero")
    else:
         print("positive")
else :
    print("negative")

# ex : 12 	Take 3 numbers and find greatest number using nested IF….ELSE statement.
x= int(input("enter any num :"))
y= int(input("enter any num :"))
z= int(input("enter any num :"))
if (x>y) :
     if (x>z):
         print("x is largest ")
     else:
         print( " z is largest")
else:
    if (z<y):
        print("y is larger")
    else:
        print("z is larger")

# ex : 13 Take 3 numbers and find smallest number using logical operator.
x= int(input("enter any num :"))
y= int(input("enter any num :"))
z= int(input("enter any num :"))
if ( x<y and x<z):
    print("x is smallest")
elif ( y<x and y<z ):
    print("y is smallest")
else:
    print("z is smallest")

# ex : 14	Write a program to swap 2 numbers without taking third variable.
x= int(input("enter any num :"))
y= int(input("enter any num :"))

print( x, y ," before swapping")
x,y = y,x

print(x,y,"after swapping")

# ex 15	Take starting number and ending number from the user and print following series.
start= int(input("enter any num :"))
end= int(input("enter any num :"))

for i in (range(start,end-1,-3)): 
   print(i)




 

