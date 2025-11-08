nums = [1,12,-5,-6,50,3]
k = 4
n=len(nums)
curr_sum=max_sum=sum(nums[:k])
for i in range(n-k):
    curr_sum+=nums[i+k]-nums[i]
    max_sum=max(max_sum,curr_sum)
print(max_sum/k)
