class Matrix:
    def Row(self,row):
        #row=int(input("enter the no of rows = "))
        self.row=row
    def Column(self,column):
        #column=int(input("enter the no of column = "))
        self.column=column
    def Set(self):
        lista=[]
        for i in range(self.row):
            listb=[]
            for j in range(self.column):
                n=int(input("enter the element of matrix= "))
                listb.append(n)
            lista.append(listb)
        print(lista)
        for x in range(self.row):
            for y in range(self.column):
                print(lista[x][y],end="  ")
            print("")
        listc=[]
        for i in range(self.row):
            listb=[]
            for j in range(self.column):
                n=int(input("enter the element of matrix= "))
                listb.append(n)
            listc.append(listb)
        print(listc)
        for x in range(self.row):
            for y in range(self.column):
                print(listc[x][y],end="  ")
            print("")
        self.lista=lista
        self.listc=listc
        
    def Adding(self):
        result=[]
        for i in range(len(self.lista)):
            r=[]
            for j in range(len(self.lista[0])):
                a=self.lista[i][j]+self.listc[i][j]
                r.append(a)
            result.append(r)
        print(result)
        for x in range(self.row):
            for y in range(self.column):
                print(result[x][y],end="  ")
            print("")
        
        
    #def Multiply(self):
        
m=Matrix()
m.Row(2)
m.Column(2)
m.Set()
m.Adding()














##    
##    def __init__(self,row,column):
##        self.row=row
##        self.column=column
##        lista=[]
##        
##        for i in range(self.row):
##            listb=[]
##            for j in range (self.column):
##                n=int(input("enter the elements of matrix="))
##                listb.append(n)
##            lista.append(listb)
##        print(lista)
##        for x in range(self.row):
##            for y in range(self.column):
##                print(lista[x][y],end="  ")
##            print("") 
##        print("")
##m=Matrix(3,3)


        
    

        
