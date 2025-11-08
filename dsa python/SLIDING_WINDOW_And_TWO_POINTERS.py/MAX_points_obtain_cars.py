nums = [9,7,7,9,7,7,9]
k = 7
n=len(nums)
left_sum=0
right_sum=0
maxim=0
for i in range(k):
    left_sum+=nums[i]

maxim=left_sum
right_ind=n-1
for i in range(k-1,-1,-1):
    left_sum-=nums[i]
    right_sum+=nums[right_ind]
    maxim=max(maxim,left_sum+right_sum)
    right_ind-=1

print(maxim)