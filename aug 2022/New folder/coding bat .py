

str=input("enter a sring= ")
if len(str)>2:
    if "." in str:
        x=str.find(".")
        for i in range (0,x):
            if str[i:3]=="xyz":
                print (True)
        
    elif "." not in str:
        for i in range(0,len(str)-3):
            if str[i:i+3]=="xyz":
                print (True)
            else:
                print (False)
else:
    print (False)

