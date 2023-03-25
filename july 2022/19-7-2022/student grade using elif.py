m=float(input("enter the percentage ="))
if(m>0 and m<=100):    
    if(m>90) and (m<=100):
        print("your grade is A")
    elif(m<=90) and (m>80):
        print("your grade is B")
    elif(m<=80) and (m>60):   
        print("your grade is C")
    elif(m<=60) and (m>=35):
        print("your grade is D")
    else:
        print("your grade is F")
else:
    print("invalid input")
