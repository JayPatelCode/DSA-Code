nums=[5,9,3,4,1,2,6]
res=[]
target=7
def back_tracking(i,total,subset):
    if total==target:
        res.append(subset)
        return True
    elif total>target:
        return False
    if i>=len(nums):
        return False
    
    subset.append(nums[i])
    pick=back_tracking(i+1,total+nums[i],subset)
    if pick==True:
        return True
    subset.pop()
    not_pick=back_tracking(i+1,total,subset)
    return not_pick

back_tracking(0,0,[])
print(res)


# TC O(2^N)
# SC(O(N)) here n is stack space