
###last digit divisble 3 or not

##n=int(input("enter a number ="))
##lastdigit=n%10 
##print("last digit is =",lastdigit)
##rem=lastdigit%3
##if(rem==0)and(lastdigit!=0):
##    print("divisible by 3")
##else:
##    print("not divisible by 3")


### divisible by two numbers

##n=int(input("enter a number="))
##if(n%2==0)and(n%3==0):
##    print(f"{n} is divisible by 2 and 3")
##elif(n%2==0):
##    print(f"{n} is divisible 2 only")
##elif(n%3==0):
##    print(f"{n} is divisible 3 only")
##else:
##    print(f"{n} is not divisible 2 and 3")
    
    
# find youngest and oldest person

a=int(input("enter a people1 age="))
b=int(input("enter a people2 age="))
c=int(input("enter a people3 age="))
d=int(input("enter a people4 age="))
if(a!=0)and(b!=0)and(c!=0)and(d!=0)and(a<=110)and(b<=110)and(c<=110)and(d<=110):
    
    if(a<b)and(a<c)and(a<d):
        print(f"people1 is youngst person")
    elif(a>b)and(b<c)and(b<d):
        print(f"people2 is youngst person")
    elif(a>c)and(b>c)and(c<d):
        print(f"people3 is youngst person")
    elif(a>d)and(b>d)and(c>d):
        print(f"people4 is youngst person")
    elif(a==b)and(a==c)and(a==d):
        print("all are same age")
    if(a>b)and(a>c)and(a>d):
        print(f"people1 is oldest person")
    elif(a<b)and(b>c)and(b>d):
        print(f"people2 is oldest person")
    elif(a<c)and(b<c)and(c>d):
        print(f"people3 is oldest person")
    elif(a<d)and(b<d)and(c<d):
        print(f"people4 is oldest person")
    
    
else:
    print("pls enter valid age")



























    
