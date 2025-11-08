# BRUTE

class Solution:
    def solve(self,index,total,nums,target,result,subset):
        if total==target:
            result.add(tuple(subset.copy()))
        elif total>target:
            return 
        if index>=len(nums):
            return

        subset.append(nums[index])
        self.solve(index+1,total+nums[index],nums,target,result,subset)
        subset.pop()
        self.solve(index+1,total,nums,target,result,subset)

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result=set()
        self.solve(0,0,candidates,target,result,[])
        return [list(r) for r in result]
    




candidates = [10,1,2,7,6,1,5]
target = 8
s=Solution()
print(s.combinationSum2(candidates,target))

# TC O(2^n * klog(k))    
# SC O(n))+O(k) here n is stack space






class Solution:
    def solve(self, index, total, nums, target, result, subset):
        if total == target:
            result.append(subset.copy())
            return
        if total > target:
            return

        for i in range(index, len(nums)):
            # skip duplicates
            if i > index and nums[i] == nums[i-1]:
                continue

            # pruning: if current number is too large, stop
            if nums[i] > target:
                break

            subset.append(nums[i])
            self.solve(i+1, total+nums[i], nums, target, result, subset)
            subset.pop()


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        self.solve(0,0,candidates,target,result,[])
        return result




# TC O(2^n * N)    
# SC O(n))here n is stack space