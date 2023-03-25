t=input("enter the time(00 hrs:00 min)= ")
d=input("enter the week day=")
l=input("enter the length of call(00 hour:00 min)")
h=int(t[:2])
m=int(t[-2:len(t)])
if m>59:
    h=h+1
weekday=["MO","TU","WE","TH","FR"]
weekend=["SA","su"]

h1=int(l[:2])
h1=h1*60

m1=int(l[-2:len(l)])
if m1>59:
    h=h+1
    m1==00
time=h1+m1

if h>0 and h<24 and m>=0 and m<60 :
    if h>=8 and h<=18 and (m>=0 and m<60):
        if d in weekday:
            cost=0.25*time
    elif (h>=18 and h<24) or (h>=1 and h<=8) and (m>0 and m<60):
        if d in weekday:
            cost=0.15*time
    elif d in weekend :
        cost=0.15*time
print ("your bill=",cost)
print(h,m,h1,m1,time)


        
        
        
        
        
