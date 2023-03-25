class area:
    
    def setDim(self,length,width):
        self.length=length
        self.width=width
        
           
    def getArea(self):
        a=self.length*self.width        
        print("area of rectangle =",a)
a=area()
a.setDim(2,4)
a.getArea()
