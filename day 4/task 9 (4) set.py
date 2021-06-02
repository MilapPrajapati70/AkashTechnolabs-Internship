# Create a class called scheme with scheme_id, scheme_name,outgoing_rate, and message_charge. 
# Derive customer class form scheme and include cust_id, name 
# and mobile_no data.Define necessary functions to read and display data.


class scheme:
    
    def setdatascheme(self):
        print("please provide your scheme names : ")
        provide1 = (input("enter 1 : "))
        provide2 = (input("enter 2 : "))
        self.provide1 = provide1
        self.provide2 = provide2
        print("your scheme name is : ",self.provide1 , "||" , self.provide2 )

        press = int(input(f"press 1 for  ({self.provide1}) or 2 for ({self.provide2}): "))
        if press == 1 :
            print("outgoing_charge = 2.0 , message charge= 1.0 ")
        elif press == 2 :
            print("outgoing_charge = 2.5 , message_charge = 0.5 ")
        else :
            print("please enter 1 or 2. ")

class customer(scheme):
     def setdatacustomer(self):
        self.cust_id= int(input("enter cust_id :"))
        self.cust_name= input("enter customer name :")
        self.mobile_no = int(input("enter customer mobile no :"))

     def showdatacustomer(self):
         print(f'{self.cust_name}  has cutomer id :  {self.cust_id}  and mobile numer {self.mobile_no}')

cls = customer()
cls.setdatacustomer()
cls.setdatascheme()
cls.showdatacustomer()






