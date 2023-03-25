a=int(input("enter your age= "))
s=int(input("your sex male=1 or female=0 ="))
n=int(input("enter number of days your worked= "))
#if(a==0)and(a<41):

if(a>18)and(a<41)and(s==0)or(s==1):
    
    if(a>=18)and(a<30)and(s==1):
        w=n*700
        print("your total wages is =",w)
    elif(a>=18)and(a<30)and(s==0):
        wages=n*750
        print("your total wages is =",wages)
    elif(a>=30)and(a<=40)and(s==1):
        wages=n*800
        print("your total wages is =",wages)
    elif(a>=30)and(a<=40)and(s==0):
        wages=n*850
        print("your total wages is =",wages)
else:
    print("enter appropriate details")   
    



