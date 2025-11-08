# nums=[1,2,3,3,3,3,3,3,5,6,8,9,9,10]
# target=3
# n=len(nums)
# first=-1
# last=-1
# for i in range(n):
#     if nums[i]==target:
#         if first==-1:
#             first=i
#         last=i
# if first==-1:
#     print([-1,-1])
# else:
#     print([first,last])

















##########OPTIMAL########
# def lower(nums,target):
#     n=len(nums)
#     l=0
#     h=n-1
#     lb=-1
#     while l<=h:
#         mid=(l+h)//2
#         if nums[mid]>=target:
#             if nums[mid]==target:
#                 lb=mid
#             h=mid-1
#         else:
#             l=mid+1
#     return lb

# def upper(nums,target):
#     n=len(nums)
#     l=0
#     h=n-1
#     up=-1
#     while l<=h:
#         mid=(l+h)//2
#         if nums[mid]>target:
#             h=mid-1
#         else:
#             if nums[mid]==target:
#                 up=mid
#             l=mid+1
#     return up

# return([lower(nums,target), upper(nums,target)])