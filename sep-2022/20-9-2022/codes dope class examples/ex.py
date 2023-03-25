class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def Area(self):
        area=self.length*self.width
        print("area of Rectangle = ",area)
r1=Rectangle(4,5)
r1.Area()
r2=Rectangle(5,8)
r2.Area()
