##
##
##for i in range(1,10):
##    for j in range(1,6):   
##        if i>=j and i<6:
##            print(j,end=" ")
##          
##        elif i<=j and i>=5 :
##            print(j,end=" ")
##    print("")     
##        

##
##tuple1=(10,20,30,40)
##a=list(tuple1)
##print(type(a))
##print(a)

##a=[10,20,30,40,50]
##b=a.copy()
##c=list(a)
##b.append(60)
##print(a)
##print(b)
##c.append(70)
##print(c)

##thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
##
##thistuple=200
##if "m" in "mango":
##    print(type(thistuple))
##    print("yes it is present in the tuple")
##else:
##    print("no")

myList=list(thistuple)
myList.append("grapes")
thistuple=tuple(myList)
print(thistuple)







