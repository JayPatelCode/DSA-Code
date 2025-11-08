#########brute

# nums=[19,4,2,11,6,5,3,10]
# n=len(nums)
# res=[]
# for i in range(n):
#     great=-1
#     for j in range(i+1,n):
#         if nums[j]>nums[i]:
#             great=nums[j]
#             break
#     res.append(great)
    
# print(res)





# optimal
nums=[19,4,2,11,6,5,3,10]
n=len(nums)
stack=[]
res=[-1] * n

for i in range(n-1,-1,-1):
    while stack and stack[-1]<=nums[i]:
      stack.pop()

    if stack:
      res[i]=stack[-1]

    
    stack.append(nums[i])

print(res)