# nested if examples:

b=1
c=1

k=int(input("enter how many kelometer covered = "))
if(k!=0):
    
    if(k<=10):
        b=k*11
        print(f"your total bill is= {b}")
    elif(k<10)and(k<=90):
        a=(k-10)
        b=(a*10)+(10*11)
        print(f"your total bill is= {b}")
    elif(k>90):
        a=(k-10)
        b=(a-80)
        c=(b*9)+(80*10)+(10*11) 
        print(f"your total bill is= {c}")
    
else:
    print("pls enter a valid km")
    
    
    

##
##e=int(input("enter your english mark= "))
##m=int(input("enter your maths mark= "))
##s=int(input("enter your science mark= "))
##s1=int(input("enter your  mark= social science= "))
##
##if(e!=0)and(e<=100)and(m!=0)and(m<=100)and(s!=0)and(s<=100)and(s1!=0)and(s1<=100):
##    if(e>80)and(m>80)and(s>80)and(s1>80):
##        print("science stream")
##    elif(e>80)and(m>50)and(s>50):
##        print("commerce stream")
##    elif(e>80)and(s1>80):
##        print("humantus stream")
##    else:
##        print("No stream avilable for your marks")
##else:
##    print("kindly enter valid marks")
##
##
###and(e>80)and(m>50)and(s>50)and(s1>80)
















    

