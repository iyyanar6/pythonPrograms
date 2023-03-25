list1=[]
l=int(input("enter length of the list= "))
for i in range(0,l):
    n=int(input("enter a number="))
    list1.append(n)

print(list1)
for a in range(0,l-1):
    for b in range(a+1,l):
        if list1[a]<list1[b]:
            pass
        elif list1[a]>list1[b]:
            list1[a],list1[b]=list1[b],list1[a]
##            temp=list1[b]
##            list1[b]=list1[a]
##            list1[a]=temp
print("after sorting" ,list1)
dif=list1[l-1]-list1[0]
print("diffrence of minimum and maximum values of list1 is= ",dif)

