##for i in range(1,5):
##    if(i==4):
##        break
##    print(i)
##else:
##    print("else is working")


##n=int(input("enter a number"))
##count=0
##for i in range(2,n):
##    if(n%i==0):
##       count+=1
##       break
##if(count==0):
##    print(n,"is a prime number")
##else:
##    print(n,"is not a prime number")
c=0
n=int(input("enter a number= "))
for i in range(2,n):
    if n%i==0:
        print(n, "is not a prime number")
        break
else:
    print(n,"is prime number")
        
