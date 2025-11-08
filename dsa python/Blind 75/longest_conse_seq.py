
################Brute#############
# nums=[100,2,200,1,3,2,4]
# n=len(nums)
# max_len=0

# for i in range(n):
#     count=0
#     num=nums[i]
#     count+=1
#     while num+1 in nums:
#       count+=1
#       num+=1
#     max_len=max(max_len,count)
    
# print(max_len)


###########BETTER############

# nums=[100,2,200,1,3,2,4]
# n=len(nums)
# last_smallest=float("-inf")
# longest=0
# count=0
# nums.sort()

# for i in range(n):
#     num=nums[i]
#     if num-1==last_smallest:
#         count+=1
#         last_smallest=num
#     elif num!=last_smallest:
#         count=1
#     last_smallest=num
#     longest=max(longest,count)
# print(longest)

# O(nlogn+n)
# O(1)



################OPTIMIZED 1#############
nums=[100,2,200,1,3,2,4]

n=set(nums)
print(n)
longest=0
for num in nums:
    if num-1 not in n:
        next_num = num + 1
        length=1
        while next_num in n:
            length+=1
            next_num+=1

        longest=max(longest, length)

print(longest)