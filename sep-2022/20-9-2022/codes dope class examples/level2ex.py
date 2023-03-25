class Matrix:
    def __init__(self,row,column):
        self.row=row
        self.column=column
        lista=[]
        
        for i in range(self.row):
            listb=[]
            for j in range (self.column):
                n=int(input("enter the elements of matrix="))
                listb.append(n)
            lista.append(listb)
        print(lista)
        for x in range(self.row):
            for y in range(self.column):
                print(lista[x][y],end="  ")
            print("") 
        print("")
m=Matrix(3,3)


        
    

        
