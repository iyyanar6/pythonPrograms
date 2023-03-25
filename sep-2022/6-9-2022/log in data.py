data={"IYYANAR":{"password":"sam@12345","name":"iyyanar"},"SAM":{"password":"123456789","name":"sam"}}
def login():
    UserName=input("enter your user name= ")
    key=data.keys()
    if (UserName in key):
        password=input("enter password= ")
        if data[UserName]["password"]==password:
            print("hello ",data[UserName]["name"])
            return
        else:
            print("do you wants to change password\n")
            n=int(input("0 for retry \n1 for forget password\n2 for new account\n"))
            if n==0:
                login()
            elif n==1:
                password1=input("enter password= ")
                password2=input("re enter password= ")
                if password1==password2:
                    data[UserName]["password"]=password1
                    login()
            elif n==2:
                dict1={}
                UserName=input("enter user name= ")
                password=input("enter password= ")
                name=input("enter your name= ")
                dict1["password"]=password
                dict1["name"]=name
                data[UserName]=dict1
                print(data)
                login()
    else:
        print("user name not in data\ndo you want create new account")
        n=int(input("0 for retry \n1 for new account\n2 for exit\n"))
        if n==0:
            login()
        elif n==1:
            dict1={}
            UserName=input("enter user name= ")
            password=input("enter password= ")
            name=input("enter your name= ")
            dict1["password"]=password
            dict1["name"]=name
            data[UserName]=dict1
            print(data)
            login()
        elif n==2:
            pass          
login()

