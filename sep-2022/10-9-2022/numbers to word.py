n= int(input("enter a number= "))

word0={1:"One hundred and",2:"Two hundred and",3:"Three hundred and",4:"Four hundred and",5:"Five hundred and",6:"Six hundred and",7:"Seven hundred and",8:"Eight hundred and",9:"Nine hundred and"}

word1={1:"eleven",2:"Twelve",3:"Thirteen",4:"Fourteen",5:"Fifteen",6:"Sixteen",7:"Seventeen",8:"Eighteen",9:"Nineteen"}

word2={1:"Ten",2:"Twenty",3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}

word3={2:"twenty",3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}

word4={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
     

l=len(str(n))
print(l)
n=str(n)
z=" "
def demo(w,z):
    
    x=n[i]
    x=int(x)
    y=w[x]
    z=y+z
    print(z,end=" ")
    str(n)

for i in range(0,l):
    if l==3:
        demo(word0,z)
        l-=1
    elif l==2 and (n[l-1])=="0":
        if n[l-2]=="1":
            demo(word2,z)
            break
    elif l==2 and (n[l-2])=="1":
        demo(word1,z)
        break
    elif l==2 :
        demo(word2,z)
        l-=1
    elif l==1:
        demo(word4,z)
        break

        
        





