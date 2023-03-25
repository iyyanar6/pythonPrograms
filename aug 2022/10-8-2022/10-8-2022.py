nums=[11,2,3]
if len(nums)>2:
    list1=[]
    if nums[0]>nums[len(nums)-1]:
        for i in range(0,len(nums)):
            list1.append(nums[0])
    elif nums[0]<nums([len(nums)-1]):
        for i in range(0,len(nums)):
            list1.append(nums[len(nums)-1])
print(list1)
  
