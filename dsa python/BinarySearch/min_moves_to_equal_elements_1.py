#########BETTER####
nums = [1,2,3]
# n=len(nums)
# mini=min(nums)
# steps=0
# for i in nums:
#    steps+=i-mini
# return steps
    
########OPTIMAL######
print(sum(nums)-(len(nums)*min(nums)))