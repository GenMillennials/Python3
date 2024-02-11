nums=[2,6,3,9]
target=15
ind=[]
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j]==target: 
            break
        else:
            print("No match")
print(nums[i],nums[j])
n=nums.index(nums[i])
print(n)
m=nums.index(nums[j])
print(m)
indices=[m,n]
print(indices)