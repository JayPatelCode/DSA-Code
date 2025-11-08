from collections import deque

#brute
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# n=len(nums)
# res=[]
# for i in range(n-k+1):
#     maxi=float("-inf")
#     for j in range(i,i+k):
#         maxi=max(maxi,nums[j])
#     res.append(maxi)
        
# print(res)


nums = [1,3,-1,-3,5,3,6,7]
k = 3

l=0

deq=deque()
result=[]
for r in range(len(nums)):
    while deq and nums[deq[-1]]<nums[r]:
        deq.pop()
    deq.append(r)

    if l>deq[0]:
        deq.popleft()

    if (r+1)>=k:
        result.append(nums[deq[0]])
        l+=1
    
print(result)



