nums=[5,7,3,2,6,1,5,9]


# def rev(nums,to,till):
    
#     if to>=till:
#         return
    
#     nums[to],nums[till]=nums[till],nums[to]
#     rev(nums,to=to+1,till=till-1)
#     return nums
    
# print(rev(nums,2,5))

n=[True if x%2==0 else False for x in range(len(nums))]
print(n)