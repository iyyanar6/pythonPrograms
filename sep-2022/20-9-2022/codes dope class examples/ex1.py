class Area:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def returnArea(self):
        a=self.length*self.breadth
        return a
a=Area(4,2)
b=a.returnArea()
print("area of rectangle is ",b)
