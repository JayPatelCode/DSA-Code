nums = [4,3,10,9,8]
nums.sort(reverse=True)
total=sum(nums)
curr=0
res=[]
for num in nums:
    curr+=num
    res.append(num)
    
    if curr> total - curr:
        break
print(res)    