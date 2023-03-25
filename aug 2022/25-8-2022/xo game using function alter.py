player1=input("enter your name= ")
player2=input("enter your name= ")
print("posotion must be 1 to 9")
listb=[]
a="_"

for i in range(0,3):
    list1=[]
    for j in range(0,3):
        list1.append(a)
    listb.append(list1)
print("")
for x in range(0,3):
    for y in range(0,3):
        print(listb[x][y],end=" ")
    print(" ")

    
def function1(x,player,n):
    if n==1:
        listb[0].pop(0)
        listb[0].insert(0,x)
           
    elif n==2:
        listb[0].pop(1)
        listb[0].insert(1,x)
        
    elif n==3:
        listb[0].pop(2)
        listb[0].insert(2,x)
        
    elif n==4:
        listb[1].pop(0)
        listb[1].insert(0,x)
        
    elif n==5:
        listb[1].pop(1)
        listb[1].insert(1,x)
        
    elif n==6:
        listb[1].pop(2)
        listb[1].insert(2,x)
        
    elif n==7:
        listb[2].pop(0)
        listb[2].insert(0,x)
        
    elif n==8:
        listb[2].pop(1)
        listb[2].insert(1,x)
        
    elif n==9:
        listb[2].pop(2)
        listb[2].insert(2,x)
                  
    for i in range(0,3):
        for j in range(0,3):
            print(listb[i][j],end=" ")
        print(" ")

    if listb[0][0]==x :
        if listb[0][1]==x and listb[0][2]==x:
            return("winner")
                    
                  
        elif listb[1][0]==x and listb[2][0]==x: 
            return("winner")
                    
        elif listb[1][1]==x and listb[2][2]==x:
            return("winner")
                    
    elif listb[1][0]==x and listb[1][1]==x and listb[1][2]==x:
            return("winner")
                
    elif listb[2][0]==x:
        if listb[2][1]==x and listb[2][2]==x:
            return("winner")
                    
        elif listb[1][1]==x and listb[0][2]==x:
            return("winner")
                    
    elif listb[0][1]==x and listb[1][1]==x and listb[2][1]==x:
        return("winner")
                
    elif listb[0][2]==x and listb[1][2]==x and listb[2][2]==x:
        return("winner")
def function2(winner):        
    lista=[]
    listc=[1,2,3,4,5,6,7,8,9]
    c=1
    while True:
        
        n=int(input( f"{player1}enter your position"))
        if n<0 and n>10 :
            print("enter valid position")
            break
        
        if n not in lista:
            lista.append(n)
            f=function1("x",player1,n)
            listc.remove(n)
            if f=="winner":
                print(player1,f)
                break
        elif n in lista:
            print(f"{n}th position already entered pls enter alternate number")
            n=int(input( f"{player1}enter your position"))
            lista.append(n)
            listc.remove(n)
            f=function1("x",player1,n)
            if f=="winner":
                print(player1,f)
                break
        c+=1
        
        n=int(input( f"{player2}enter your position"))
        
        if n not in lista:
            lista.append(n)
            f=function1("o",player2,n)
            listc.remove(n)
            if f=="winner":
                print(player2,f)
                break
        elif n in lista:
            print(f"{n}th position already entered pls enter alternate number")
            n=int(input( f"{player2}enter your position"))
            lista.append(n)
            listc.remove(n)
            f=function1("o",player2,n)
            
            if f=="winner":
                print(player2,f)
                break
        c+=1
        
        if c>9:
            print("match drawn")
            break
    
function2(1)
   
























