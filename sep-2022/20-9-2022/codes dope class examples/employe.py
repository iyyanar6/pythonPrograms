class Employee:
    def __init__(self,name,year_of_joining,address):
        self.name=name
        self.year_of_joining=year_of_joining
        self.address=address
e=Employee("Robert",1994,"64C-Wallsstreet")
print("name     year of joining     address")
print(e.name,end="       ")
print(e.year_of_joining,end="            ")
print(e.address)

e1=Employee("sam",2000,"68D-Wallsstreet")
#print("name     year of joining     address")
print(e.name,end="       ")
print(e1.year_of_joining,end="            ")
print(e1.address)

e2=Employee("john",1999,"26B-Wallsstreet")
#print("name     year of joining     address")
print(e2.name,end="         ")
print(e2.year_of_joining,end="            ")
print(e2.address)
