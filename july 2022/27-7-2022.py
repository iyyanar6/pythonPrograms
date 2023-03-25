##a="iyyanar"
##length=len(a)
###print(length)
###for i in range(1,length,1):
##print(a)

start=int(input("enter a start number= "))
stop=int(input("enter a end number= "))
for i in range(start,stop+1):
    for j in range(2,i):
        if(i%j==0):
##            print(i,"is not a prime number")
            break
    else:
        print(i,"is prime number")
    
        
        
   
    
