list1=[]
l=int(input("enter length of the list="))
for i in range(0,l):
    n=int(input("enter values of list="))
    list1.append(n)
print(list1)
for j in range(0,l):
    a=j+1
    if a<l:
        b=list1[a]-1
        if list1[j]==b:
            pass
        else:
            b=list1[j]+1
            print(b,"missing in the number order")
       
