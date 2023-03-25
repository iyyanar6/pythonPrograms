lista=[]
row1=int(input("enter the number of list1 rows= "))
col1=int(input("enter the number of list1 col= "))
for i in range(0,row1):
    list1=[]
    for j in range(0,col1):
        n=int(input("enter the number="))
        list1.append(n)
    print(list1)
    lista.append(list1)
print(lista)
print("")
for x in range(0,row1):
    for y in range(0,col1):
        print(lista[x][y],end=" ")
    print("")
listb=lista.copy()
print(listb)
print("")
for c in range(0,row1):
    for d in range(0,col1):
        print(lista[c][d],end=" ")
    print("")
print("")
listc=[]
print("addition of two matrix")
for j in range(0,row1):
    list2=[]
    for k in range(0,col1):
        m=lista[j][k]+listb[j][k]
        print(m,end="  ")
        list2.append(m)
    listc.append(list2)
    print("")
print("")
print(listc)
        

