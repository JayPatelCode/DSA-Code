#########better######

# arr=[2,4,6,6,6,6,6,6,6,6,7,7,9,11,18,18,19]
# target=3
# count=0
# n=len(arr)
# for i in range(n):
#     if arr[i]==target:
#         count+=1
# print(count)


#######OPTIMAL######


# arr=[2,4,6,6,6,6,6,6,6,6,7,7,9,11,18,18,19]
# target=3
# n=len(arr)
# def lower(arr,target):
#     n=len(arr)
#     l=0
#     h=n-1
#     lb=-1
#     while l<=h:
#         mid=(l+h)//2
#         if arr[mid]>=target:
#             if arr[mid]==target:
#                 lb=mid
#             h=mid-1
#         else:
#             l=mid+1
#     return lb

# def upper(arr,target):
#     n=len(arr)
#     l=0
#     h=n-1
#     up=n
#     while l<=h:
#         mid=(l+h)//2
#         if arr[mid]>target:
#             h=mid-1
#         else:
#             if arr[mid]==target:
#                 up=mid
#             l=mid+1
#     return up
# lb=lower(arr,target)
# ub=upper(arr,target)
# if lb==-1:
#     return 0
# return(ub-lb+1)