#WITH OUT PARAMETER

##class Triangle:
##    
##    def __init__(self,s1,s2,s3):
##        self.side1=s1
##        self.side2=s2
##        self.side3=s3
##        area=self.side1*self.side2*self.side3
##        print("area of tirangle is",area)
##        perimeter=self.side1+self.side2+self.side3
##        print("perimeter of a triangle",perimeter)
##        
##t=Triangle(3,4,5)



#WITH  PARAMETER

class Triangle:
    side1=3
    side2=4
    side3=5
    def __init__(self):
        area=self.side1*self.side2*self.side3
        print("area of tirangle is",area)
        perimeter=self.side1+self.side2+self.side3
        print("perimeter of a triangle",perimeter)
        
t=Triangle()














