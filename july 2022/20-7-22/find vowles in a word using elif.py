#                   find vowels in character
##
##c=input("pls enter any letter ")
##if("a" in c):
##    print("a is vowle")
##elif("e" in c):
##    print("e is vowle")
##elif("i" in c):    
##    print("i is vowle")
##elif("o" in c):
##    print("o is vowle")
##elif("u" in c):
##    print("u is vowle")
##else:
##    print(" this letter not a vowle")


#find vowels in character
b=0
n=input("pls enter any letter= ")
l=len(n)
##b=n.count("a")
for i in range(0,l):
    if("a" in n[i]):
        b+=1
for i in range(0,l):
    if("e" in n[i]):
        b+=1
for i in range(0,l):
    if("i" in n[i]):
        b+=1
for i in range(0,l):
    if("o" in n[i]):
        b+=1
for i in range(0,l):
    if("u" in n[i]):
        b+=1
print(f"{b} times vowles are prsented in the string")


##    print("a is vowle")



##elif("e" in c):
####    print("e is vowle")
##elif("i" in c):    
####    print("i is vowle")
##elif("o" in c):
####    print("o is vowle")
##elif("u" in c):
####    print("u is vowle")
##else:
####    print(" this letter not a vowle")
##
##
##












    
