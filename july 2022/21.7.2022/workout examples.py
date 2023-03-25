
#average of numbers using for loop

##
##a=0
##b=int(input("enter a number ="))
##for i in range(0,b,1):
##    n=int(input("enter a number="))
##    
##    a=a+n
##
##avg=a/b
##print("total =",a)
##print("average is =",avg)
##

### find  factorial of any number using for loop
##a=1
##b=int(input("enter a number for factorial ="))
##for i in range(1,b+1,1):
##    
##    a=a*i
##
##print(a)


#find whether the number is prime of not

n=int(input("enter a number="))
#m=n/2
#m=int(m)
for i in range(0,n//2,1):
    if(n%1!=0) and (n%n!=0):
        print(f"{n} is a prime number")
        
    else:
        print(f"{n} is not a prime number")

            





















