##import functools
##lista=[1,2,3,4,5,6,7,8,9,10]
##print("sum of list elements is =",end=" ")
##
##print(functools.reduce(lambda a,b:a+b,lista))
##print("maximum element in the list=",end=" ")
##print(functools.reduce(lambda a,b:a if a>b else b,lista))

##import functools
##import operator
##lista=[1,2,3,4,5,6,7,8,9,10]
##print("sum of list elements is =",end=" ")
##print(functools.reduce(operator.add,lista))
##print("product of the list=",end=" ")
##print(functools.reduce(operator.mul,lista))
##print(functools.reduce(operator.add,["a","b","c"]))

#NON LOCAL VARIABLES

##def demo():
##    x="hello"
##    def demo1():
##        nonlocal x
##        x="world"
##        print(x)
##    demo1()
##    print(x)
##demo()

#FILTER

##lista=[1,3,6,4,5,6,7,8,9,10]
##def demo(x):
##    if x>5:
##        return True
##    else:
##        return False
##a=filter(demo,lista)
##print(list(a))


#REDUCE

##import functools
##import operator
##lista=[1,3,4,5,6,7]
##a=functools.reduce(operator.add,lista)
##b=functools.reduce(operator.mul,lista)
##
##print(b)
##print(a)


#local ,global and non-local variables


##a=1 #global variable
##def demo():
##    b=2  #local varialble
##    def demo1():
##        nonlocal c  # nonlocal variable
##        c=3
##    demo1()
##demo()
##






















