#bonus calculation using elif

n=int(input("enter a number of working years="))
s=int(input("enter your current salary amount="))

if(n!=0)and(n<=40):
      if(n>10):
          print("you get 10% bonus amount")
          t=s*10/100
          p=s+t
          p=int(p)
          print(f"your total salary after bonus additin= {p} Rs")
      elif(n<=10)and(n>=6):
          print("you get 8% bonus amount")
          t=s*8/100
          p=s+t
          p=int(p)
          print(f"your total salary after bonus additin= {p} Rs")
      elif(n<6):
          print("you get 5% bonus amount")
          t=s*5/100
          p=s+t
          p=int(p)
          print(f"your total salary after bonus additin= {p} Rs")
else:
    print("pls enter valid working year")
    
    
