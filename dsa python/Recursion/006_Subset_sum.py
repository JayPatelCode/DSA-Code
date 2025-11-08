class Solution:
    def solve(self,total,index,arr,result):
        if index>=len(arr):
            result.append(total)
            return
        self.solve(total+arr[index],index+1,arr,result)
        self.solve(total,index+1,arr,result)


    def subsetSums(self, arr):
        result=[]
        self.solve(0,0,arr,result)
        return result
    

arr = [2, 3]
s1=Solution()
print(s1.subsetSums(arr))


# TC O(2^N)
# SC(O(N)) here n is stack space