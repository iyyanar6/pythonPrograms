##lista=[1,2,3,4,5,6,7]
##lista=str(lista)
##def demo(n):
##    add=0
##    for i in n:
##        add=+int(i)
##    return add
##print(list(map(demo,lista)))
##
##lista=[]
##
##for i in range(0,4):
##    n=int(input("enter a number"))
##    lista.append(n)
##print(lista)
##def demo(n):
##    c=0
##    
##    for i in n:
##        c=c+i
##        
##    return (c)
##c=demo(lista)
##print(c)

data={"IYYANAR":{"password":"sam@12345","name":"iyyanar"},"SAM":{"password":"123456789","name":"sam"},'SAVI': {'password': '12345', 'name': 'savitha'}}
data["SAVI"]["name"]="iyyanar"
print(data["SAVI"]["name"])
