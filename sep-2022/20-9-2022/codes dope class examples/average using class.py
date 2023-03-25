class Average:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def calculate(self):
        avg=(self.a+self.b+self.c)/3
        print(int(avg))
a=Average(2,4,6)
a.calculate()
a1=Average(4,6,8)
a1.calculate()
