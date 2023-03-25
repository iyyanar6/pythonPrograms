#factorial using function


##n=int(input("enter a number= "))
##def function1(n):
##    a=1
##    for i in range(1,n+1):
##        a=a*i
##    return(a)
##f=function1(n)
##print("factorinal of given number is=",f)

#even digit sum


##n=int(input("enter a number= "))
####
##def function1(n):
##    x=0
##    while True:
##        a=n%10
##        n=n//10
##        if a>1:
##            if a%2==0:
##                x=x+a
##        else:
##            break
##        
##    return(x)
##f=function1(n)
##print("even digit sum is",f)      
    
   
#addition of first and last digit of inter

##n=int(input("enter a number= "))
##n1=n
##if n<0:
##    n=-(n)
##print(n)
##def function1(n):
##    a=n%10
##    if a==n:
##        return(a+n)
##    while True:
##        b=n%10
##        n=n//10
##        if n>=1:
##            pass
##        else:
##            return(a+b)
##f=function1(n)
##if n1<0:
##    f=-(f)
##print("first and last digit sum is= ",f)      
    

#last digit checker
n=int(input("enter number of cheking="))
lista=[]
print("numbers must be 10-1000")
for i in range(0,n):
    n1=int(input("enter a number= "))
    lista.append(n1)
print(lista)
def function1(lista):
    for x in lista:
        if x<10 or x>1000:
            return( False)
    listb=[]
    for j in lista:
        l=j%10
        listb.append(l)
    for i in range(0,(len(listb)-1)):
        for j in range(i+1,len(listb)):
            if listb[i]==listb[j]:
                return True
    return False
f=function1(lista)
print(f)

    










































