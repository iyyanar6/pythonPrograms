##import demo1
##file=open("text.txt","r")
##file=open("text.txt","w")
##file.write("hello world")
##c=demo1.add(2,4)
##c=str(c)
##file.write(f"\naddition of two integer is= {c}")
##file.close()



##from head import demo
##from head import demo1
##print(demo.sub(10,5))
##print(demo1.add(10,5))


##from head import demo
##from head import demo1
##file=open("text.txt","r")
##file=open("text.txt","w")
##file.write("hello")
##file=open("text.txt","a")
##s=demo.sub(10,6)
##a=demo1.add(10,6)
##file.write(f"\nsubtraction of two number is= {s}")
##file.write(f"\n addition of two number is = {a}")
##file.close()
##
##a=int(input("enter 1st number= "))
##b=int(input("enter 2st number= "))
##c=int(input("enter 3st number= "))
##if a>b and a>c:
##    print(f"{a} is grater than {b} and {c}")
##elif b>a and b>c:
##    print(f"{b} is grater than {a} and {c}")
##elif c>a and c>b:
##    print(f"{c} is grater than {a} and {b}")
##elif a==b and a>c:
##    print((f"{a} and {b} are same value and grate than {c}"))
##elif a==c and a>b:
##    print((f"{a} and {c} are same value and grate than {b}"))
##elif a==b and a<c:
##    print((f"{c} is grater than {a} and {b}"))
##elif a==c and a<b:
##    print((f"{b} is grater than {a} and {c}"))
##elif b==c and b>a:
##    print(f"{b} and {c} are same values and grater than {a}")
##elif b==c and b<a:
##    print(f"{a} is grater than {b} and {c}")
##elif a==b and a==c:
##    print("three numbers are same values")
##    
##
##n=int(input("enter a number= "))
##for i in range(2,n):
##    if n%i==0:
##        print(n, "is not prime number")
##        break
##else:
##    print(n, "is a prime number")

import re
a="hello world"
x=re.findall("[h]",a)
print(x)








    
