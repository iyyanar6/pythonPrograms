n=int(input("enter a number= "))
list1=[]
list2=[]
if n>0:
    for x in range(1,n):
        if (n%x==0):
            print(x)
            list1.append(x)
print(list1)
for i in list1:
    if i>1:
        c=0
        for j in range(2,i):
            if i%j==0:
                c+=1      
        if c==0:
            list2.append(i)
print(list2)
print(list2[0],"is smalest prime number in list")
print(list2[(len(list2)-1)],"is largest prime number in list")
##        
##c=0
##list2=[]
##list1=[1,2,3,6]
##for i in list1:
##    if i>1:
##        for j in range(2,i):
##            if i%j==0:
##                c+=1
##                
##        if c==0:
##            list2.append(i)
##print(list2)







          
