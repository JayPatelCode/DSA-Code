nums=[5,9,3,4,1,2,6]
target=7
def subsequence(index,total):
    if total==target:
        return 1
    elif total>target:
        return 0
    if index>=len(nums):
        return 0
    
    pick=subsequence(index+1, total+nums[index])
    print(pick)
    
    not_pick=subsequence(index+1, total)
    print(not_pick)

    return pick+not_pick

print(subsequence(0,0))


# TC O(2^N)
# SC(O(N)) here n is stack space
