##
a=0
b=1

n=int(input("enter a number for fibonaci series= "))
print(f"first {n} fibonaci series is = ",end="")

print(a,b,end=" ")
for i in range(2,n,1):


    c=a+b
    a=b
    b=c
    print(c,end=" ")
   
    


#leap year calculation
##
##y=int(input("enter a year= "))
##if(y>999)and(y<=9999):
##
##    if(y%4==0):
##        if(y%100==0)and(y%400==0):
##            print(f"{y} is leap year")
##        elif(y%100==0)and(y%400!=0):
##            print(f"{y} is not leap year")
##        elif(y%100!=0):
##            print(f"{y} is leap year")
##
##            
##    else:
##        print(f"{y} is not a leap year")
##    
        
    




















    
    
