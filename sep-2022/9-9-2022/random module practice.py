##import random
##
##def demo():
##    
##    x=random.randint(0,9)
##    y=int(input("enter a number o to 9= "))
##    if x==y:
##        return "you win"
##    else:
##        print("random number is",x)
##        demo()
##
#RANDOM NUMBER SINGLE DIGIT 

##print(demo())
##import random
##while True:
##    x=random.randint(0,9)
##    y=int(input("enter a number o to 9= "))
##    if x==y:
##        print("you win")
##        break
##    else:
##        print("random number is",x)
##        print("try again")
##    
#RANDOM OTP

##import random
##print(random.randint(1000,9999))
##


#NUMBERS TO WORDS
n= int(input("enter a number= "))
word={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
z=" "
while(True):
    
    x=n%10
    if n>0:
        
        y=word[x]
        y=y.capitalize()
        z=y+" "+z
        
    elif x<1:
        break
    n=n//10
print(z,end=" ")   




















