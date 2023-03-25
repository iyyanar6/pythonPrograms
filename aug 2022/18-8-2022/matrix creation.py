rows=int(input("enter number of rows= "))
col=int(input("enter nuber of columns= "))
lista=[]
for i in range(1,rows+1): 
    listi=[]
    for x in range(0,col):
        n=int(input("enter the list elements= "))
        listi.append(n)
    print(listi)

    lista.append(listi)
    
print(end="")
print(lista)
print("")

for x in range(0,len(lista)):
    for y in range(0,len(lista[x])):
        print(lista[x][y],end=" ")
        
    print("")
##    
##sumOfValues=0
##dic={1:10,2:20,3:30,4:40,5:50}
####print(dic.values())
##for i,j in dic.items():
##    print(i,j)
####    sumOfValues+=dic[i]
####print(sumOfValues)
##
##
##
##
##






















