list1=[1,2,3,4,2,4,5,6,5]
for i in list1:
    a=list1.count(i)
    
    if a>1:
        print(f"{i} is repeated {a} times")
        list1.remove(i)
