class Circle:
    def __init__(self,radius):
        if radius<0:
            self.radius=0
        else:
            self.radius=radius
        
    def area(self):
        a=3.14*self.radius
        print("area of a circle",a)
class Cylinder(Circle):
    def __init__(self,radius,height):
        super().__init__(radius)
        if height<0:
            self.height=0
        else:
            self.height=height
        
    def volume(self):
        volume=3.14*((self.radius)**2)*self.height
        print("volume of a cylinder is",volume)
c=Cylinder(2,3)
c.area()
 c.volume()

        
