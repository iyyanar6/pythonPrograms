##n=int(input("enter a number = "))
##for i in range(2,n//2,1):
##    if(n%i==0):
##        print(n,"is not  prime number")
##        break
##else:
##    print(n, " is prime number")
##



    
##a=0
##for i in range(2,n//2):
##    if(n%i==0):
##        a+=1
##if(a==0):
##    print("is a prime number")
##else:
##    print("is not a prime number")



#for i in range(0,n,1):
n=int(input("enter a number= "))
a=0
while(n!=0):
    m=n%10
    x=n//10
    n=x
    a=a*10+m
    #print(m)
    
    if(x==0):
        break
print("revers digit a=",a)














    
    
