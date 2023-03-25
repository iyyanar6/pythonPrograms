class mobile:
    def __init__(self,model,colour,ram,price):
        self.model=model
        self.colour=colour
        self.ram=ram
        self.price=price
        print("model :",model)
        print("colour :",colour)
        print("ram :",ram)
        print("price :",price)
    def camera(s,model):
        return ("can access camera in ",s.model)
    def music(s,model):
        print("can play",s.model," clear music")
        
m1=mobile("oppo","black","4 GB",15000)
print(m1.camera("32 MP"))
m1.music("5.1")
print("")
m2=mobile("vivo","blue","6 GB",20000)
print(m2.camera("64 MP"))
m2.music("5.1")




        
