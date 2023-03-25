##
##
##for i in range(1,8):
##    a=10
##    for j in range(1,8):
##        if i>=j:
##            
##            print(a,end=" ")
##            a-=2
##    print('')
##
##output
##    
## 10 
## 10 8 
## 10 8 6 
## 10 8 6 4 
## 10 8 6 4 2 


##for i in range(0,7):
##    a=0
##    for j in range(0,7):
##        if i>=j:
##            
##            print(a,end=" ")
##            a+=i
##    print('')
##
##
##output
##
## 0 
## 0 1 
## 0 2 4 
## 0 3 6 9 
## 0 4 8 12 16 
## 0 5 10 15 20 25 
## 0 6 12 18 24 30 36 

a=1
for i in range(0,7):
    for j in range(0,7):
        if i!=j:
            print("*",end=" ")
          
##            a-=1
##            if i==a:
##                b+=1
##                print(b,end=" ")
    print('')





















