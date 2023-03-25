list1=[]
list2=[]
l1=int(input("enter first list length="))
l2=int(input("enter second list length="))
for i in range(0,l1):
    n=int(input("enter values of list1="))
    list1.append(n)
print(list1)
for j in range(0,l2):
    m=int(input("enter values of list2="))
    list2.append(m)
print(list2)
list3=[]
for x in list1:
    for y in list2:
        if x==y:
            list3.append(x)
print("common values in both list is= ",list3)
