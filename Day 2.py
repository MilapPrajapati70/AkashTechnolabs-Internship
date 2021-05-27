#task 1
a=10
b=9.5
c= "Milap"

print("value of a is :", a)
print("value of b is :", b , type(b))
print(c)

#task 2
name = "khalidja tuesday"

print(name)
print(name[0:8])
print(name[:10])
print("namaste ", name)

#task 3

list1 = [ 20,3.9,352,"Milap"]

print("list1 ="  ,list1)
print(list1[2])

list =[]
x= int(input("enter number of elemts in list :"))
for i in range(0,x):
    element=input("enter value of element :")
    list.append(element)
print(list)    

#task 4

tuple1 = ( 10,46,7.7, "pluto")
print( " tuple1[2] :", tuple1[2])
print(tuple1[1:3])

list =[]
x= int(input("enter number of elemts in list :"))
for i in range(0,x):
    element=input("enter value of element :")
    list.append(element)
tup = tuple(list)    
print(list)    
print(tup)

# task 5 

d = {1 : "milap", 2: "prajapati", 3: 9}
print(d[3])


