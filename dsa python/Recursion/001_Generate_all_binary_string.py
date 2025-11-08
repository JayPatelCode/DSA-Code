class Solution:
    def solve(self, flag, index, numbers,result):
        if index>=len(numbers):
            result.append("".join(numbers))
            print(result,"Res")
            return
        
        numbers[index]="0"
        self.solve(True,index+1,numbers,result)
        if flag==True:
            numbers[index]="1"
            self.solve(False,index+1,numbers,result)
            numbers[index]="0"
            
    
    def generateBinaryStrings(self, n):
        numbers=["0"] * n
        result=[]
        self.solve(True,0,numbers,result)
        return result
    



s=Solution()
print(s.generateBinaryStrings(3))
