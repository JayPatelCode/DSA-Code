nums=[2,10,12,1,11]
n=len(nums)
res=[-1]*n
stack=[]

for i in range(2*n-1,-1,-1):
    while stack and nums[stack[-1]]<=nums[i%n]:
        stack.pop()

    if stack:
        res[i%n]=nums[stack[-1]]
    stack.append(i%n)

print(res)


# nums=[2,10,12,1,11]
# n=len(nums)
# res=[-1]*n
# stack=[]

# for i in range(2*n-1,-1,-1):
#     while stack and stack[-1]<=nums[i%n]:
#         stack.pop()

#     if stack:
#         res[i%n]=stack[-1]
#     stack.append(nums[i%n])

# print(res)










