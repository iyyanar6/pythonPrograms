l=int(input("enter lenth of the list= "))
list1=[]
for i in range(0,l):
    n=int(input("enter values of the list= "))
    list1.append(n)
print(list1)

for x in range(0,l-1):
    for y in range(x+1,l):
        a=0
        if list1[x]<list1[y]:
            pass
        else:
            a=list1[y]
            list1[y]=list1[x]
            list1[x]=a
print(list1)
print("second largest number in above list =",list1[l-2])
        
