##class phone:
##    brand="vivo"
##    price=10000
##    weight="190 grm"
##    colour="black"
##    def music(s,a):
##        print("can play songs")
##        print(a)
##    def game(s):
##        print("this mobile phone can access high graphics game")
##    def call(self):
##        print("can make any call at any time")
##p1=phone()
##print(p1.brand)
##print(p1.price)
##p1.colour="white"
##print(p1.colour)
##p1.music("hello")
##
##
##print("")
##p2=phone()
##p2.brand="apple"
##print(p2.brand)
##print(p2.price)
##print(p2.colour)
##p2.music("hi")

##my=lambda *a:len(a)
##a=my("apple","banana","cherry")
##print((a))


lista=[12,23,5,67,56]
def demo(x):
    
    if x>18:
        return True
    else:
        return False
adult=filter(demo,lista)
    
#x=functools.reduce(lambda *a:len(a[1]),lista)

for i in adult:
    print(i)
























