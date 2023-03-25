lista=[]
r=int(input("enter no of rows ="))
c=int(input("enter no of columns ="))
for i in range(r):
    list1=[]
    for j in range(c):
        n=int(input("enter a number ="))
        list1.append(n)
    lista.append(list1)
    print(list1)
print (lista)
print(" ")

for x in range(r):
    for y in range(c):
        print(lista[x][y],end="  ")
    print("")
print(" ")
for x in range(r):
    for y in range(c):
        print(lista[y][x],end="  ")
    print("")

    
