n=5
class Solution:
    def solve(self,col,board,left_row,lower_diagonal,upper_diagonal,result,n):
    
        if col==n:
            result.append(board[:])
            return
        for row in range(n):
            if left_row[row]==0 and lower_diagonal[row+col]==0 and upper_diagonal[n-1+col-row]==0:
                board[row]=board[row][:col]+"Q"+board[row][col+1:]
                left_row[row]=1
                lower_diagonal[row+col]=1
                upper_diagonal[n-1+col-row]=1
                self.solve(col+1,board,left_row,lower_diagonal,upper_diagonal,result,n)
                board[row]=board[row][:col]+"."+board[row][col+1:]
                left_row[row]=0
                lower_diagonal[row+col]=0
                upper_diagonal[n-1+col-row]=0

    def solution(self,n):
        result=[]
        board=["." * n for _ in range(n)]
        left_row=[0]*n
        lower_diagonal=[0]*(2*n-1)
        upper_diagonal=[0]*(2*n-1)
        self.solve(0,board,left_row,lower_diagonal,upper_diagonal,result,n)
        return result

s=Solution()
print(s.solution(4))