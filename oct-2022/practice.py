##
##class Temprature:
##    def __init__(self):
##        pass
##    def ConvertFahrenheit(self):
##        celsius=float(input("enter celsius value= "))
##        self.celsius=celsius
##        F=(celsius*(9/5)+32)
##        f=round(F,2)
##        
##        print( f"Equlent Fahrenheit value is {f} F" )
##    def ConvertCelsius(self):
##        Fahrenheit=float(input("enter Fahrenheit value= "))
##        self.Fahrenheit=Fahrenheit
##        C=(Fahrenheit-32)*(5/9)
##        c=round(C,2)
##        print(f"Equlent Celsius value is {c} C")
##t=Temprature()
##t.ConvertFahrenheit()
##t.ConvertCelsius()

class Student:
    def __init__(self,name,rollNo):
        self.name=name
        self.rollNo=rollNo
    def Display(self):
        print("name : ",self.name)
        print("Roll NO : ",self.rollNo)
    def setAge(self):
        age=int(input(f"enter {self.name} age= "))
        self.age=age
    def setMarks(self):
        tamil=int(input("enter tamil mark = "))
        english=int(input("enter english mark= "))
        maths=int(input("enter maths mark= "))
        science=int(input("enter science mark= "))
        socialscience=int(input("enter socialscience mark= "))
        self.tamil=tamil
        self.english=english
        self.maths=maths
        self.science=science
        self.socialscience=socialscience
    def getMarksheet(self):
        print("name : ",self.name)
        print("Roll NO : ",self.rollNo)
        print("age : ",self.age)
        print("")
        print("Tamil : ",self.tamil)
        print("English : ",self.english)
        print("maths : ",self.maths)
        print("science : ",self.science)
        print("socialscience : ",self.socialscience)
        

s=Student("iyyanar",1001)
s.Display()
s.setAge()
s.setMarks()
s.getMarksheet()




        

        






