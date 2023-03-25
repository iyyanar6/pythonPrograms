#calculate student attendence perccentage and eligiblity of examination

t=int(input("enter the total no of working days="))
a=int(input("enter the total no of days for absent="))
if(a!=0)and(t!=0)and(t<=30)and(a<=30)and(a>0)and(t>0):
    s=t-a
    p=s/t*100
    p=int(p)
    print(f"attend class days percentage of the student is = {p} %")
    if(p>75):
        print("the student is eligible for sit in exam")
    else:
         print("the student is not eligible for sit in exam")
    
else:
    print("pls enter the valid information")
