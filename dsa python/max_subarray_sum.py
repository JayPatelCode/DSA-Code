######Brute force###33

# nums=[-2,1,-3,4,-1,2,1,-5,4]
# max_sub_array=float("-inf")
# n=len(nums)
# for i in range(n):
#     sum=0
#     for j in range(i,n):
#         sum=sum+nums[j]
#         max_sub_array=max(max_sub_array,sum)

# print(max_sub_array)



nums=[-2,1,-3,4,-1,2,1,-5,4]
max_sub_array=float("-inf")
sum=0
n=len(nums)

for i in range(n):
    sum+=nums[i]
    max_sub_array=max(sum,max_sub_array)
    if sum<0:
        sum=0

print(max_sub_array)