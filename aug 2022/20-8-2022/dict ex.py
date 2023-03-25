u=int(input("enter how many students informarion you have= "))
lista=[]
for i in range(1,u+1):
    list1=["name","age","sex","mark"]
    dic={}
    for j in list1:
        n=input(f"enter the {j} = ")
        dic[j]=n
    lista.append(dic)
print(lista)
