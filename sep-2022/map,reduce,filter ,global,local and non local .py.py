#LAMBDA

##x=lambda a,b:a+b
##print(x(2,3))


#FUNCTION AND MAP

##lista=[1,2,3,4,5,6]
##def demo(n):
##    return (2+n)
##print(list(map(demo,lista)))

#LAMBDA AND MAP

##lista=[1,2,3,4,5,6]
##print(list(map(lambda a:a+2,lista)))

#FILTER

##lista=[1,2,3,4,5,6]
##def demo(n):
##    if n%2==0:
##        return True
##    else:
##        return False
##print(list(filter(demo,lista)))


#REDUCE

##lista=[1,2,3,4,5,6]
##import functools
##x=functools.reduce(lambda a,b:a*b,lista)
##print(x)


#LOCAL ,GLOBAL AND NON-LOCAL VARIABLES

##a=10    #global
##def demo():
##    a=20    #local
##    print(a)
##    def demo1():
##        nonlocal a  # non-local
##        a=30
##        print(a)
##    demo1()    
##    print(a)
##demo()
##print(a)


x=10
def demo():
    

















