##def demo1(a,b):
##    print (a+b)
##def demo2(a,b):
##    print(a-b)

##def demo():
##    
##    try:
##        n=int(input("enter a number = "))
##        print(n)
##    except ValueError:
##        print("enter a interger number")
##        demo()
##    finally:
##        return("square of give number is=",n*2)
##    
##print(demo())

for i in range(0,10):
    for j in range(0,5):
        if i>=j and i<5:
            
            print("*",end=" ")
    for k in range(0,5):
        if i<=k:
            print("*",end=" ")
    print("")
    
        
