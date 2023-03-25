a=1
for i in range(1,6,1):
    a=i
    for j in range(1,6,1):
        if(i>=j):
            print(a,end=" ")
            a-=1     
    print(" ") 
        
