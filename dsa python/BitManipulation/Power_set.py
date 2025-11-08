
# 2 raise to n == 1<<n

# [[]]
# [[], [1]]
# [[], [1], [2]]
# [[], [1], [2], [1, 2]]
# [[], [1], [2], [1, 2], [3]]
# [[], [1], [2], [1, 2], [3], [1, 3]]
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3]]


# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

nums=[1,2,3]
n=len(nums)
total_subset=1<<n
result=[]
for num in range(0,total_subset):#########0 to 7 here if n=3 and here subsets are 8.
    lst=[]
    for i in range(n):
        if num & (1<<i)!=0:
            lst.append(nums[i])
    result.append(lst)
    # print(result)
print(result)

# TC:O(n* 2^n)
# sc