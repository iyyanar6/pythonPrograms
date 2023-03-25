n=int(input("enter a number= "))
m=n
c=0
while n>0:
    a=n%10
    n=n//10
    b=1
    for i in range(1,a+1):
        b=b*i
    print(b)
    c=c+b
if c==m:
    print(m,"is strong number")
else:
    print(m,"is not strong number")

#output

##enter a number= 145
##120
##24
##1
##145 is strong number
