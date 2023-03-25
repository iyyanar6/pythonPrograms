##roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
##num=[1,5,10,50,100,500,1000]
##n=input("enter your roman number = ")
##add=0
##for i in range(0,(len(n)-1)):
##    if roman[n[i]]==roman[n[i+1]]:
##        add=add+roman[n[i]]
##    elif roman[n[i]]>roman[n[i+1]]:
##        add=add+roman[n[i]]
##    elif roman[n[i]]<roman[n[i+1]]:
##        add=add-roman[n[i]]
##   
##add=add+roman[n[-1]]
##print(add)
##

#ADD TWO NUMBERS

lista=[]
listb=[]
n=int(input("enter lengthe of the list="))
for i in range(0,n):
    m=int(input("enter elements of list= "))
    lista.append(m)
print(lista)
t=int(input("enter a target= "))
for j in range(0,n-1):
    for k in range(1,n):
       if lista[j]+lista[k]==t :
           listb.append(j)
           listb.append(k) 
           print(listb)
    break
