
y=0
a=int(input("enter a integer number = "))
n=int(input("enter total value= "))
if(a>1)and(n%a==0):
    #while(n>=2):
    
    for i in range(0,n,1):
        x=n/a
        n=x
        y+=1
        if(n==a):
            break
    y+=1    
    print(f"eponent of {a} is {y}")

else:
    print("enter a valid values")
    



