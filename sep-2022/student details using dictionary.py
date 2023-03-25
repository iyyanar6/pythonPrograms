dict1={}
n=int(input("enter a length of dictionary= "))
for i in range(n):
    dict2={}
    roll=int(input("enter roll number="))
    name=input("enter student name= ")
    sex=input("enter student sex= ")
    age=int(input("enter student age= "))
    dict2["name"]=name
    dict2["age"]=age
    dict2["sex"]=sex
    "roll"
    dict1[roll]=dict2
print(dict1)
print("")
detail=int(input("enter roll number show student detail= "))
print("")           
#print(dict1[detail])
for x,y in dict1[detail].items():
    print(x,":",y)
