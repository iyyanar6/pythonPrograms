##class Student:
##    def __init__(self,name,roll_no):
##        self.name=name
##        self.roll_no=roll_no
##s=Student("john",2)
##print("name : ",s.name)
##print("roll_no : ",s.roll_no)
##
##s1=Student("sam",3)
##print("\nname : ",s1.name)
##print("roll_no : ",s1.roll_no)

class Student:
    def __init__(self,name,roll_no,phone,address):
        self.name=name
        self.roll_no=roll_no
        self.phone=phone
        self.address=address
        
s=Student("john",1,8124233033,"143,west st,gandhithirunallur,puducherry")
print("name : ",s.name)
print("roll_no : ",s.roll_no)
print("phone : ",s.phone)
print("address : ",s.address)

s1=Student("sam",2,9442160584,"153,gandhi st,mettupalayam,puducherry")
print("\nname : ",s1.name)
print("roll_no : ",s1.roll_no)
print("phone : ",s1.phone)
print("address : ",s1.address)













