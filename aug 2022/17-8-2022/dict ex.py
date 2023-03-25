##d={"name":"iyyanar","age": 24,"roll no":1607,"mark":72}
##print (d)
l=int(input("enter the total number of students="))
total=[]
for j in range(1,l+1):
    a=["name","age","roll no","mark"]
    mydict={}
    for i in a:
        b=input(f"enter {i}{j} =")
        mydict[i]=b
    print(mydict)
    total.append(mydict)
print(total)
