class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        n=len(s)
        last={}
        for i in range(n):
            last[s[i]]=i
        print(last)
        result=[]
        size,end=0,0
        for i,v in enumerate(s):
            size+=1
            end=max(end,last[v])
            if i==end:
                result.append(size)
                size=0
        return result

sol=Solution()
s = "ababcbacadefegdehijhklij"

print(sol.partitionLabels(s))
