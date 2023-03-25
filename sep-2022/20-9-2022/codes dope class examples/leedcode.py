##if len(s)>1:
##    for i in range(0,len(s),2):
##        if i=="(":
##            if i+1==")":
##                return True
##            else:
##                return False
##        elif i=="[":
##            if i+1=="]":
##                return True
##            else:
##                return False
##        elif i=="{":
##            if i+1=="}":
##                return True
##            else:
##                return False
##else:
##    return False
##        
##x=sqrt(x)
##print(x)

##lista=[1,2,5]
##listb=[1,3,4]
##lista.extend(listb)
##print(lista)
##lista.sort()
##print(lista)


lista=[1,2,5]
listb=[1,2,3,4]
listc=[]
d=[]
count=0
lista.extend(listb)
print(lista)
for i in range(len(lista)):
    if lista[i] not in listc:
        listc.append(lista[i])
    else:
        d.append("_")
        
listc.sort()
listc.extend(d)
print(listc)












