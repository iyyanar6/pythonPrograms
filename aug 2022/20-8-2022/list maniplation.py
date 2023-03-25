lista=[1,3,4,2,5,7,6,9]
while True:
    print("list maniplication")
    print("\n1 for add elements \n2 for modify elements \n3 for delete elements \n4 for sort list \n5 for display list\n6 for exit \n")
    a=int(input("enter your choise="))
    
    if a==1:
        x=int(input("1 for add one element \n2 for add mutiple elements\n"))
        if x==1:
            n=int(input("enter a number = "))    
            lista.append(n)
        if x==2:
            m=int(input("how many number you wants to enter="))
            for i in range(1,m):
                n=int(input(f"enter a number {i} = "))
                lista.append(n)
        print (lista)            
    elif a==2:
        print("list modification")
        x1=int(input("1 for change specific index value\n2 for change specific value"))
        if x1==1:
            i=int(input("enter index= "))
            if i in lista:
                j=int(input("enter a value new value="))
                x=len(lista)
                lista[i]=j
            else:
                print("invalid index\n")
                continue
        elif x1==2:
            i=int(input("enter a values to be change"))
            if i in lista:
                i1=lista.index(i)
                lista.pop(i1)
                j=int(input("enter alternate value"))
                lista.insert(i1,j)
            else:
                print("entered value not in list")
                continue
        print(lista)
    elif a==3:
        i=int(input("1 for delete index\n2 for delete value"))
        if(i==1):
            j=int(input("enter index="))
            x=len(lista)
            if j>=x:
                print("invalid index\n")
                continue
            else:
                lista.pop(j)
        elif (i==2):
            j=int(input("enter a value"))
            if j in lista:
                lista.remove(j)
            else:
                print("entered number is not in list\n")
                continue
        print(lista)
    elif a==4:
        x2=int(input("enter 1 for ascending order \nenter 2 for decending order="))
        listb=lista.copy()
        if x2==1:
            listb.sort()    
        elif x2==2:
            listb.reverse()
        print(listb)
    elif a==5:
        print (lista)
    elif a==6:
        break













        
                
            
            
                
            
