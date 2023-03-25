##def demo(a):
##    return(a+10)
##add=demo
##def demo1():
##    print("output",add(5))
##demo1()

##
##class parent:
##    def __init__(self):
##        pass
##    def demo1(self):
##        return("hello")
##child=parent
##c=child()
##def demo():
##    print(c.demo1())
##demo()

##def demo(func):
##    print("demo is running")
##    def inner(a,b):
##        print("i am going to divide" ,a,b)
##        if b==0:
##            print(f"any number can't be divided by {b} ")
##            return
##        return func(a,b)
##    return inner
##        
##    
##
##@demo
##def demo2(a,b):
##    print("demo2 is running")
##    print(a/b)

##demo2(10,2)

def secondfunc(func):
    def inner(name):
        print("#"*30)
        func(name)
        print("#"*30)
    return inner
def firstfunc(func):
    def inner(name):
        print("hello ",name)
        func(name)
        print("thank you")
    return inner
@secondfunc
@firstfunc

def demo(name):
    print("good morning")
name=input("enter your name")
demo(name)































