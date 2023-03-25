
##class DemoError(Exception):
##    def __init__(self,num):
##        self.num=num
##    def __str__(self):
##        return f"DemoError:given number is zero kindly entered another number"
##try:
##    n=int(input("enter a number ="))
##    if n==0:
##        raise DemoError(n)
##except DemoError as d:
##    print (d)
##    
    
def sub(a,b):
    s=a-b
    return s
