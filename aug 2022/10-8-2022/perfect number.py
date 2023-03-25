n=int(input("enter a number= "))
c=0
if n>0:
    for i in range(1,n):
        if (n%i==0):  
            print(i)
            c=c+i
print(" ")        
print(c)
if c==n:
    print(n,"is perfect number")
else:
    print(n,"is not perfect number")

