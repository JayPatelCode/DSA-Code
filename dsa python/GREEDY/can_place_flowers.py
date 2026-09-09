class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        f=[0]+flowerbed+[0]
        print(f)
        for i in range(1,len(f)-1):
            if f[i-1]==0 and f[i]==0 and f[i+1]==0:
                f[i]=1
                n-=1
        return n<=0
    
flowerbed = [1,0,0,0,1]
n = 1
c=Solution()
print(c.canPlaceFlowers(flowerbed,n))
