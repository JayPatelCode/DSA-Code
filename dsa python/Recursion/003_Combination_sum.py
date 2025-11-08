class Solution:
    def solve(self,index,total,subset,nums,target,result):
        if total==target:
            result.append(subset.copy())
            return
        elif total>target:
            return
        if index>=len(nums):
            return
        

        subset.append(nums[index])
        self.solve(index,total+nums[index],subset,nums,target,result)
        subset.pop()
        self.solve(index+1,total,subset,nums,target,result)

        
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]
        self.solve(0,0,[],candidates,target,result)
        return result
    






# TC O(2^t * k)        where t is the total time we can pick one element and k is time to copy element
# SC O(t))+O(k) here n is stack space