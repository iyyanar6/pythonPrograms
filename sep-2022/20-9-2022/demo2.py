class mobile:
    def __init__(self,brand,colour,price):
        self.brand=brand
        self.colour=colour
        self.price=price
    def music(s,a):
        print("this mobile has good sound at play music")
        print(s.brand)
        print(a)
    def video(a):
        print(a.colour)
        print("good pictre quality when play a video file")
m1=mobile("blackberry","white",15000)
print(m1.brand)
print(m1.colour)
print(m1.price)
m1.music("hello")
m1.video()
print("")
m2=mobile("redmi","black",10000)
print(m2.brand)
print(m2.colour)
print(m2.price)
m2.colour="green"
m2.music("hi")
m2.video()
print("")
m3=mobile("realme","black",17000)
print(m3.brand)
print(m3.colour)
print(m3.price)
#m2.colour="green"
m3.music("world")
m3.video()
