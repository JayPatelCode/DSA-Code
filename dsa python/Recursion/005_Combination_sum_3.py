class Solution:
    def solve(self, last, total, subset, n, k, result):
        if total==n and len(subset)==k:
            result.append(subset.copy())
            return
        
        if total>n and len(subset)>k:
            return

        for i in range(last,10):
            subset.append(i)
            self.solve(i+1, total+i, subset, n, k, result)
            subset.pop()

        
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result=[]
        self.solve(1,0,[], n, k, result)
        return result
    


k = 3
n = 7
s=Solution()
print(s.combinationSum3(k,n))



# TC: O(k⋅(k9​))
# SC: O(k) for recursion + result storage.