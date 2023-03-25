def secondfunc(func):
    print("second function is running")
    def inner(*a):
        print("#"*30)
        func()
        print("$"*30)
    return inner
def firstfunc(func):
    print("first function is running")
    def inner(*a):
        print("hi")
        func()
    return inner

@secondfunc
@firstfunc
def demo(*a):
    print("hello")
demo(3)
