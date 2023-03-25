class UserError(Exception): 
    def __init__(self,msg):
        self.msg=msg
        

try:
    number=int(input("enter a number= "))
    if number>0 and number<100:
        pass
    else:
        raise UserError("entered number is must between 0 and 100")
    
except UserError as e:
    print("UserError :",e.msg)


0
