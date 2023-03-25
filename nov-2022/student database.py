print("STUDENT REGISTRATION")

       
def new():
    roll_No=int(input("enter Roll No : "))
    name=input("enter name : ")
    age=int(input("enter age : "))
    DOB=input("enter Date of Birth : ")
    mark=int(input("enter mark : "))
    course=input("enter your course : ")
    global dict1
    dict1={}
    
    
    dict1["Roll_No"]=roll_No
    dict1["Name"]=name
    dict1["Age"]=age
    dict1["Date_of_Birth"]=DOB
    dict1["Mark"]=mark
    dict1["Course"]=course
    print("complete")
    register()
    
def retrive():
    print(dict1)
    print("which data your want")
    find=input("Mark\nAge\nCourse\n see all details for enter ALL")
    if find=="Mark":
        print(dict1["Mark"])
    elif find=="Age":
        print(dict1["Age"])
    elif find=="Course":
        print(dict1["Course"])
    elif find=="ALL":
        for x,y in dict1.items():
            print(x," : ",y)
    register()
        
def update():
    print("which details you want update your details:")
    change=input("Mark\nCourse")
    if change=="Mark":
        mark=int(input("enter new Mark : "))
        dict1["Mark"]=mark
    elif change=="Course":
        dict1["Course"]=course
    register()
def show():
    print("do you want see updated details")
    detail=input("yes\nno")
    if detail=="yes":
        for x,y in dict1.items():
            print(x," : ",y)
    register()
    
def delete():
    print("which detail you want delete")
    remove=input("Mark\nCourse\n delete all details for enter ALL")
    if remove=="Mark":
        mark=int(input("enter new Mark : "))
        dict1["Mark"]=mark
    elif remove=="Course":
        dict1["Course"]=course
    elif remove=="ALL":
        del dict1
        print("delete complete")
lista=[1,2,3,4]
def register():
    data=int(input(" new Accout for enter 1 : \n find data in record enter 2\n update data in record enter 3\n delete data in record enter 4\n 0 fo exit\n"))
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



