##print("hello iyyanar")
##print("hello sam")
##try:
##    print("hello")
##except:
##    print("error")
##for i in range(5):
##    print("hello")
####print(2+4)
##f=open("sam1.txt","w")
##f.write("hello \n sam")
##try:
##    f=open("sam1.txt","a")
##    f.write(hello)
##except:
##    f=open("sam1.txt","a")
##    f.write("\nworld")
##
##finally:
##
##    f=open("sam1.txt","r")
##    for i in f:
##        print(i)
##    
##    f.close()


t=50
def demo():
    n=int(input("enter no of tickets= "))
    global t
    a=t-n
    print("aviable tickets =",a)
    if a==0:
        
        return
    t=a
    demo()
    
demo()

