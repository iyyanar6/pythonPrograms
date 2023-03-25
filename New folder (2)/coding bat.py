##nums=[1,2,3,4,5,6]
##if len(nums)>0:
##    count=0
##    for i in nums:
##        even=i%2
##        if even==0 or i==0:
##            count+=1
##return count


##a=[10,3,4,6,7]
##for i in range(len(a)-1):
##    for j in range(i+1,len(a)):
##        if a[i]<a[j]:
##            pass
##        else:
##            c=a[i]
##            a[i]=a[j]
##            a[j]=c
##print(a)
##dif=a[-1]-a[0]
##print(dif)

##import math
##a=[10,3,4,8,7,7]
##if len(a)>2:
##    d=len(a)/2
##    d=str(d)
##    print(d)
##    if d[-1]==0:
##        a=d[0]
##        d=int(a)
##        print(d)
##        avg=(a[c-1]+a[c])/2
##        print(avg)
##        
##    else :
##        d=len(a)/2
##        c=math.floor(d)
##        print(a[c])
##nums=[1, 2, 1, 2]
##def has22(nums):
##    if len(nums)>0:
##        if 2 in nums:
##            x=nums.index(2)
##            print(x)
##            if nums[x+1]==2:
##                print( True)
##            else:
##                print(False)
##        else:
##            print( False)
##  
##    else:
##        print(False)
##has22(nums)
##import math
##num1=[1,3,5]
##num2=[2,4]
##num1.extend(num2)
##num1.sort()
##
##div=len(num1)/2
##s=str(div)
##print(s)
##if s[-1]=="0":
##    div=len(num1)/2
##    x=math.floor(div)
##    add=(num1[x]+num1[x-1])/2
##    print(add)
##else:
##    div=len(num1)/2
##    x=math.floor(div)
##    print(num1[x])


x=1245
result=0
count=0
if x<0:
    count=1
    x=-x
while True:
    n=x%10
    x=x//10
    print(x)
    if x>0:
        result=n*10+result
    

        











































