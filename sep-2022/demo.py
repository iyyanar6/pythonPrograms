##import random
##lista=["apple","banana","kiwi"]
###random.seed(10)
##print(random.randint(0,100))

##lista=[1,2,3,4]
##listb=[1,2,3,4]
##l1=len(lista)
##l2=len(listb)
##for i in range(0,l1):
##    a=lista[i]+listb[i]
##    listc.append(a)

#NUMBER PALINDROME

##lista=[]
##x=121
##
##y=str(x)
##listb=list(y)
##for i in range(-1,-len(y)-1,-1):
##    lista.append(y[i])
##
##if lista==listb:
##    print (True)
##else:
##    print (False)


#
##x=1001
##y=x
##a=0
##if x<0:
##    print(False)
##else:
##    while True:
##        n=x%10
##        x=x//10
##        
##        if n>=1:
##            a=a*10+n
##        elif n==0:
##            a=10*n
##        else:
##            print(a)
##            if y==a:
##                print(True)
##            else:
##                print(False)
##            break
##        
##
###

strs = ["fower","flow","flight"]
a=strs[0]
a=a[0:2]
def demo():
    if len(strs)<2:
        return strs[0]
    else:
        a=strs[0]
        for i in range(1,len(strs)):
            if a[0]==strs[i][0:1]:
                if a[0:2]==strs[i][0:2]:
                    return a[0:2]
                return a[0]
        else:
            return ""
print(demo())











