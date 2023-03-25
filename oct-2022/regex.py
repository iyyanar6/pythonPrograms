# PAN CARD CHECKING

##import re
##string=input("enter your pan card number= ")
##pattren=r"^[A-Z]{5}\d{4}[A-Z]$"
##result=re.search(pattren,string)
##if result:
##    print("matched")
##else:
##    print("not matched")
    

##import re
##
##string=input("enter your email id= ")
##pattren=r"^\w+\S*\w*@\w+\.[a-zA-Z]{2,3}$"
##result=re.search(pattren,string)
##print(re.findall(pattren,string))
##print(result)
##if result:
##    print("matched")
##else:
##    print("not matched")




##mail=input("enter your email address= ")
##if re.search(r"^\w|\W{5,10}@gmail.com$",mail):
##    print("hello")
##else:
##    print("re enter")



##listb=[]
##lista=[1,3,5,6,5,6,7,8,9]
##c=0
##for i in range(len(lista)-1):
##    for j in range(i+1,len(lista)):
##        if lista[i]>lista[j]:
##            c=lista[i]
##            lista[i]=lista[j]
##            lista[j]=c
##print("sorted list=",lista)
##for i in lista:
##    if i not in listb:
##        listb.append(i)
##print("duplicates removed list=",listb)
##c=0
##for i in range(len(listb)):
##    c=c+1
##    if listb[i]!=c:
##        listb.insert(i,c)
##print("value low to high=",listb)
##    

        
##    if i not in listb:
##        listb.append(b)

import re
string=input("enter your gmail address= ")
pattren=r"^\w+\S*\w+@\w+\.[a-zA-Z]{2,5}$"
result=re.search(pattren,string)
if result:
    print("matched")
else:
    print("not matched")
























