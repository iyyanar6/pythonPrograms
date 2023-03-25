a=input("enter a value=")
b="mf"
c="fm"
l=len(a)
count=0
for i in range(0,l+1,2):
    
    if (a[i:i+2]==b) or (a[i:i+2]==c):
        count+=1
print(count)
