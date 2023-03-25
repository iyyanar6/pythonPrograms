set1=[1,4,3,5,1,3,5,6,6,2]
list1=[]
list2=[]
for i in set1:
    if i not in list1:
        list1.append(i)
    else:
        list2.append(i)
        
set1=list1.copy()    

print(set1)
print(list2)
    
    

