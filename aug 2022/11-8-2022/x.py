n=int(input("enter a number= "))
a,b,c=0,0,0
list1=[]
if n>0:
    for i in range(1,n):
        if (n%i==0):  
            c=c+i
            list1.append(i)
if c==n:
    print(n,"is perfect number")

    print(list1)
    for i in list1:
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break    
            else:
                print(i, "smalest prime number in list1")
                list1.reverse()
                continue   
    
##    for x in list1:
##        for y in range(2,x):
##            if(x%y==0):
##                break
##              
##        else:
##            print(x,"is largest prime number in list1")
##            break
else:
    print(n,"is not perfect number")










          
