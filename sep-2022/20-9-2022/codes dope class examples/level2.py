class Employee:
    
    def getInfo(self,salary,hour):
        self.salary=salary
        self.hour=hour

    def AddSal(self):
        if self.salary<500:
            self.salary=self.salary+10
    def AddWork(self):
        if self.hour>6:
            self.salary=self.salary+5
        
        return self.salary
e=Employee()
e.getInfo(510,7)
e.AddSal()
s=e.AddWork()
print("the final salary is= ",s)

e1=Employee()
e1.getInfo(550,7)
e1.AddSal()
s=e1.AddWork()
print("\nthe final salary is= ",s)

