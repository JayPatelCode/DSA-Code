# nums=[5,9,3,4,1]
# res=[]
# target=9
# def subsequence(index,subset):
#     if index>=len(nums):
#         if sum(subset)==target:
#             res.append(subset.copy())
#         return
    
#     subset.append(nums[index])
#     subsequence(index+1,subset)
#     subset.pop()
#     subsequence(index+1,subset)



# subsequence(0,[])
# print(res)











nums=[5,9,3,4,1,2,6]
res=[]
target=7
def subsequence(index,total,subset):
    if total==target:
        res.append(subset.copy())
        return
    elif total>target:
        return
    if index>=len(nums):
        return
    
    
    subset.append(nums[index])
    subsequence(index+1, total+nums[index], subset)
    subset.pop()
    subsequence(index+1, total,subset)



subsequence(0,0,[])
print(res)


# TC O(2^N)
# SC(O(N)) here n is stack space
