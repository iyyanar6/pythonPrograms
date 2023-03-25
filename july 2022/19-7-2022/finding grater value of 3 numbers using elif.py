

a=int(input("enter the value of a ="))
b=int(input("enter the value of b ="))
c=int(input("enter the value of c ="))
##print(a>b>c,a<b>c,a<b<c)
if(a>b)and(a>c):
    print (f"{a} is grater than {b} & {c}")
elif(a<b)and(b>c):
    print(f"{b} is grater than {a}& {c}")
elif(a<c)and(b<c):
    print(f"{c} is grater than {a} & {b}")
else:
    print(f"all three values are same")

