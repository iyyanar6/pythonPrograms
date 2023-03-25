import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")
mydb=client["StudentDatabase"]
mycol=mydb["StudentDetails"]
print("STUDENT REGISTRATION")

def new():
    roll_No=int(input("enter Roll No : "))
    name=input("enter name : ")
    age=int(input("enter age : "))
    DOB=input("enter Date of Birth : ")
    mark=int(input("enter mark : "))
    course=input("enter your course : ")
    
    dict1={}
    dict1["Roll_No"]=roll_No
    dict1["Name"]=name
    dict1["Age"]=age
    dict1["Date_of_Birth"]=DOB
    dict1["Mark"]=mark
    dict1["Course"]=course
    x=mycol.insert_one(dict1)
    print(" insert complete")
    register()
    
def retrive():
    data=int(input("find data with roll no enter 0\nfind data with name enter 1\nfind with mark enter 2\nfind with age enter 3\nfind with course enter 4\n"))
    if data==0:
        roll_No=input("enter rol_no= ")
        x=mycol.find({"Roll_No":roll_No})
        print(x)
    elif data==1:
        name=input("enter name= ")
        x=mycol.find({"Name":name})
        for i in x:
            print(i)
    elif data==2:
        mark=int(input("enter mark= "))
        x=mycol.find({"Mark":mark})
    elif data==3:
        age=int(input("enter age= "))
        x=mycol.find({"Age":age})
    elif data==4:
        course=inpur("enter course= ")
        x=mycol.find({"Course":course})
    else:
        data=int(input("ivalid input \nenter 1 for retry\nenter 2 for home "))
        if data==1:
            retrive()
        elif data==2:
            register()

def update():
    change=input("enter current course for change")
    oldvalue={"Course":change}
    alter=input("enter new course ")
    newvalue={"$set":{"Course":alter}}
    y=mycol.update_one(oldvalue,newvalue)
    print(y.modified_count,"documents updated" )
    print("update sucess")
    register()

def delete():
    remove=input("enter roll no for delete= ")
    z=mycol.delete_one({"Roll_No":remove})    
    print("delete complete")
    register()
            
        
        
lista=[1,2,3,4,0]
def register():
    data=int(input(" new student for enter 1 : \n find data in record enter 2\n update data in record enter 3\n delete data in record enter 4\n 0 fo exit\n"))
    if data in lista:
        if data==1:
            new()
        elif data==2:
            retrive()
        elif data==3:
            update()
        elif data==4:
            delete()
        elif data==0:
            return
    else:
        print("enter valid number")
        register()
register()
