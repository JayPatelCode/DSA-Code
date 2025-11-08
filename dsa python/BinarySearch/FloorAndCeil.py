##############better######333
# nums=[3,4,4,4,8,9,9,10,12,12,14,15]
# x=11
# n=len(nums)
# floor=-1
# ceil=-1
# for n in nums:
#     if n<=x:
#         if floor==-1 and n>floor:
#             floor=n
#     if n>=x:
#         if ceil==-1 and n<ceil:
#             ceil=n
# print(floor,ceil)







nums=[3,4,4,4,8,9,9,10,12,12,14,15]
x=11
n=len(nums)
floor=-1
ceil=-1
l=0
h=n-1
while l<=h:
    m=(l+h)//2
    if nums[m]==x:
        print[nums[m],nums[m]]
    elif nums[m]>x:
        h=m-1
        ceil=nums[m]
    else:
        l=m+1
        floor=nums[m]
print[floor,ceil]