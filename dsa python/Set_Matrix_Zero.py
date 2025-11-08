# 1,1,1
# 1,0,1
# 1,1,1

from typing import List


class Solution:
    def set_inf(self,matrix,row,col):
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            if matrix[i][col] !=0:
                matrix[i][col]=float("inf")
                
        for j in range(c):
            if matrix[row][j] !=0:
                matrix[row][j]=float("inf")
        
        return matrix


    def set_zero(self,matrix)->None:
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    self.set_inf(matrix,i,j)
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==float("inf"):
                    matrix[i][j]=0

num=[[0,1,1],[1,1,1],[1,1,0]]
s=Solution().set_zero(num)
print(num)

# TC: O(n*m)*(n+m)+O(n*m)










############OPTIMAL######
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        """
        Do not return anything, modify matrix in-place instead.
        """
        
        r=len(matrix)
        c=len(matrix[0])

        row_track=[0 for _ in range(r)]
        col_track=[0 for _ in range(c)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    row_track[i]=-1
                    col_track[j]=-1

        
        for i in range(r):
            for j in range(c):
                if row_track[i]==-1 or col_track[j]==-1:
                    matrix[i][j]=0

        
# TC:O(2*(n*m))
# sc:O(n+m)