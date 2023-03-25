t=0
distance=0
lista=[]
y=0
trip=int(input("enter how many trip you wants to drive= "))
for x in range(1,trip+1):
    print("TRIP",x)
    n=int(input(f"enter no pasengers (maximum 5 menbers) = "))
    list1=["pick up point","drop point","approximate km"]
    dic={}
    
    if n>0 and n>5:
        print("maximum 5 pasengers for a per trip do you wants continu or cancel trip")
        y=int(input("1 for continue\n2 for cancel"))
        if y==1:
            n=int(input(f"enter no pasengers (maximum 5 menbers) = "))
    if n>0 and n<6:
        
        pp=input(f"enter {list1[0]} =")
        dic[list1[0]]=pp
        dp=input(f"enter {list1[1]}=")
        dic[list1[1]]=dp
        akm=int(input(f"enter {list1[2]}="))
        dic[list1[2]]=akm
        distance=distance+akm
        if (n<3)and akm<55:
            a=10*akm
            print(f"bill amount of trip {x} is=",a)
            
        elif (n>=3 and n<=5 and akm<55):
            a=15*akm
            print(f"bill amount of trip {x} is=",a)
        elif (n<3 and akm>=55):
            a=(10*akm)
            b=a*0.60
            a=a+b
            print(f"bill amount of trip {x} is= ",a)

        elif (n<=5 and akm>=55):
            a=(15*akm)
            b=a*0.60
            a=a+b
            print(f"bill amount of trip {x} is= ",a)
        t=t+a
        dic["bill"]=a
        lista.append(dic)
    if y==2:
        break

##    print(dic)
print(lista)
print("total amount per day=",t)
print("total distance covered in a day=",distance)

