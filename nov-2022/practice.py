##set1={1,2,3,4,5}
##set2={3,4,6,5}
##print(len(set1 - set2))

##def add(a,b):
##    return a+5, b+5
##result=add(3,2)
##print(result)

##a=4
##b=5
##print(a<<b)
number=int(input("enter a number= "))
rev=0
for i in range(5):
    rem=number//10
    print(rem)
    
    if rem>=0:
        
        ans=number%10
        print(ans)
        rev=ans+rev*10
        number=rem
        print(rev)
        
    else:
        break
    
