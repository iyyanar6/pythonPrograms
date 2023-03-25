a=5
def calculator1():
    a=int(input("enter a number ="))
    b=int(input("enter a number= "))
    n=int(input("1 for addition \n2 for subtraction \n3 for multiplication \n4 for divition\n5 for exit\n"))
    
    if n==1:
        add=a+b
        print(f"addition of {a} and {b} is {add} ")
        calculator1()
    elif n==2:
        sub=a-b
        print(f"subtraction of {a} and {b} is {sub} ")
        calculator1()
    elif n==3:
        mul=a*b
        print(f"multioplication of {a} and {b} is {mul} ")
        calculator1()
    elif n==4:
        div=a/b
        print(f"divition of {a} and {b} is {div} ")
        calculator1()
    elif n==5:
        return
    

