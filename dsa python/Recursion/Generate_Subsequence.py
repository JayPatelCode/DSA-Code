nums=[5,9,7]
res=[]
def subsequence(index,subset):
    if index>=len(nums):
        res.append(subset.copy())
        return
    
    subset.append(nums[index])
    subsequence(index+1,subset)
    subset.pop()
    subsequence(index+1,subset)



subsequence(0,[])
print(res)







# TC O(2^N)
# SC(O(N)) here n is stack space
