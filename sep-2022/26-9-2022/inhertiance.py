class Scooty:
    def __init__(self,name,model,year,price):
        self.name=name
        self.model=model
        self.year=year
        self.price=price
    def longdrive(self):
        print("IN",self.name,"cannot sutable for longdrive")
class Bike(Scooty):
    def __init__(self,name,model,year,price,gear):
        self.gear=gear
        super().__init__(name,model,year,price)
    def comfort(self):
        print("In",self.name,"comfort for longdrive")
b=Bike("splender","sp1",2019,70000,4)
print(b.name)
b.longdrive()
b.comfort()
