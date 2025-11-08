nums = [1,10,2,9]
nums=sorted(nums)
l=0
h=len(nums)-1
mid=(l+h)//2
step=0
for i in range(len(nums)):
    step+=abs(nums[i]-nums[mid])
print(step)
