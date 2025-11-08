# ######Iterative##########3
# nums=[2,4,6,7,9,11,18,19]

# def binarySearch(nums,target):
#     low=0
#     high=len(nums)-1
    
#     while low<=high:
#         mid=(low+high)//2
#         if nums[mid]==target:
#             print(mid)
#             break
#         elif nums[mid]>target:
#             high=mid-1
#         else:
#             low=mid+1
#     print(-1)

# binarySearch(nums,7)






###########recursive#####
# nums=[2,4,6,7,9,11,18,19]

# def binarySearch(nums,low,high,target):
#     if low>high:
#         return -1
#     mid=(low+high)//2
#     if nums[mid]==target:
#         print(mid)
#     elif nums[mid]<target:
#         binarySearch(nums,mid+1,high,target)
#     else:
#         binarySearch(nums,low,mid-1,target)

# binarySearch(nums,0,len(nums)-1,7)

# TC: log2(N)
# SC: O(1)




##########3Lower bound###33
# smallest index such that nums[i]>=target
# arr=[2,4,6,6,6,7,7,9,11,18,18,19]
# x=18
# n=len(arr)
# low=0
# high=n-1
# lowerbound=-1
# while low<=high:
#     mid=(low+high)//2
#     if arr[mid]>=x:
#         lowerbound=mid
#         high=mid-1
        
#     else:
#         low=mid+1

# print(lowerbound)





##########Upper bound###33
# smallest index such that nums[i]>target
# arr=[2,4,6,6,6,7,7,9,11,18,18,19]
# x=18
# n=len(arr)
# low=0
# high=n-1
# upperbound=-1
# while low<=high:
#     mid=(low+high)//2
#     if arr[mid]>x:
#         upperbound=mid
#         high=mid-1
        
#     else:
#         low=mid+1

# print(upperbound)

# TC:log2(N)