
##for i in range(1,6):
##    a=1
##    for j in range(5,0,-1):
##        if i<=j:
##            print(a,end=" ")
##            a+=1
##    print("")      

#o/p

##1 2 3 4 5 
##1 2 3 4 
##1 2 3 
##1 2 
##1
c=1
temp=0
for i in range(1,10,2):
    a=5
    temp=c
    for j in range(10,0,-1):
        if(j-c<5 and i<=j):
            print(temp,end=" ")
            temp+=1
        elif i<=j:
            print(a,end=" ")
            a-=1
    c+=1       
    print("")      

