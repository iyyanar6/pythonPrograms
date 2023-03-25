lista=[1,2,3,4,5,6,7,8,9]
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
c=0
while True:
    n=int(input("player 1 enter your position"))
    if n>0 and n<=9:
        if n in lista :
            if n==1:
                listb[0].pop(0)
                listb[0].insert(0,"x")
                lista.remove(n)
            elif n==2:
                listb[0].pop(1)
                listb[0].insert(1,"x")
                lista.remove(n)
            elif n==3:
                listb[0].pop(2)
                listb[0].insert(2,"x")
                lista.remove(n)
            elif n==4:
                listb[1].pop(0)
                listb[1].insert(0,"x")
                lista.remove(n)
            elif n==5:
                listb[1].pop(1)
                listb[1].insert(1,"x")
                lista.remove(n)
            elif n==6:
                listb[1].pop(2)
                listb[1].insert(2,"x")
                lista.remove(n)
            elif n==7:
                listb[2].pop(0)
                listb[2].insert(0,"x")
                lista.remove(n)
            elif n==8:
                listb[2].pop(1)
                listb[2].insert(1,"x")
                lista.remove(n)
            elif n==9:
                listb[2].pop(2)
                listb[2].insert(2,"x")
                lista.remove(n)
        elif n not in lista:
            print(f"{n}th position already entered pls enter alternate number")
            continue

            
        for x in range(0,3):
            for y in range(0,3):
                print(listb[x][y],end=" ")
            print(" ")
            c=c+1
        
    
            if listb[0][0]=="x" :
                if listb[0][1]=="x" and listb[0][2]=="x":
                    print(player1,"winner")
                    break
                elif listb[1][0]=="x" and listb[2][0]=="x":
                    print(player1,"winner")
                    break
                elif listb[1][1]=="x" and listb[2][2]=="x":
                    print(player1,"winner")
                    break
                
            elif listb[1][0]=="x" and listb[1][1]=="x" and listb[1][2]=="x":
                print(player1,"winner")
                break
            elif listb[2][0]=="x" :
                if listb[2][1]=="x" and listb[2][2]=="x":
                    print(player1,"winner")
                    break
                elif listb[1][1]=="x" and listb[0][2]=="x":
                    print(player1,"winner")
                    break
               
                
            if listb[0][1]=="x" and listb[1][1]=="x" and listb[2][1]=="x":
                print(player1,"winner")
                break       
            elif listb[0][2]=="x" and listb[1][2]=="x" and listb[2][2]=="x":
                print(player1,"winner")
                break
            
        
##    else:
##        print("enter valid position")
##        break
            
        n=int(input("player 2  enter your position"))        
        if n>0 and n<=9:
            if n in lista :
                if n==1:
                    listb[0].pop(0)
                    listb[0].insert(0,"o")
                    lista.remove(n)
                elif n==2:
                    listb[0].pop(1)
                    listb[0].insert(1,"o")
                    lista.remove(n)
                elif n==3:
                    listb[0].pop(2)
                    listb[0].insert(2,"o")
                    lista.remove(n)
                elif n==4:
                    listb[1].pop(0)
                    listb[1].insert(0,"o")
                    lista.remove(n)
                elif n==5:
                    listb[1].pop(1)
                    listb[1].insert(1,"o")
                    lista.remove(n)
                elif n==6:
                    listb[1].pop(2)
                    listb[1].insert(2,"o")
                    lista.remove(n)
                elif n==7:
                    listb[2].pop(0)
                    listb[2].insert(0,"o")
                    lista.remove(n)
                elif n==8:
                    listb[2].pop(1)
                    listb[2].insert(1,"o")
                    lista.remove(n)
                elif n==9:
                    listb[2].pop(2)
                    listb[2].insert(2,"o")
                    lista.remove(n)
            elif n not in lista:
                print(f"{n}th position alreary entered pls enter alternate number")
                continue
                    
            for x in range(0,3):
                for y in range(0,3):
                    print(listb[x][y],end=" ")
                print(" ")
                c=c+1
                if listb[0][0]=="o" :
                    if listb[0][1]=="o" and listb[0][2]=="o":
                        print(player2,"winner")
                        break
                    elif listb[1][0]=="o" and listb[2][0]=="o":
                        print(player2,"winner")
                        break
                    elif listb[1][1]=="o" and listb[2][2]=="o":
                        print(player2,"winner")
                        break
                elif listb[1][0]=="o" and listb[1][1]=="o" and listb[1][2]=="o":
                    print(player2,"winner")
                    break
                elif listb[2][0]=="o" :
                    if listb[2][1]=="o" and listb[2][2]=="o":
                        print(player2,"winner")
                        break
                    elif listb[1][1]=="o" and listb[0][2]=="o":
                        print(player2,"winner")
                        break
                elif listb[0][1]=="o" and listb[1][1]=="o" and listb[2][1]=="o":
                    print(player2,"winner")
                    break
                elif listb[0][2]=="o" and listb[1][2]=="o" and listb[2][2]=="o":
                    print(player2,"winner")
                    break            
    else:
        print("enter valid position")
        break
    
    if c==9:
        print("match draw")
        


