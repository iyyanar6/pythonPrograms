
list1=[]
length=int(input("enter length of list"))
for i in range(0,length):
    a1=input("enter element of list")
    list1.append(a1)
print(list1)

result=[]
for i in list1:
    if i not in result:
        result.append(i)
print(result)
print("original list",list1)


