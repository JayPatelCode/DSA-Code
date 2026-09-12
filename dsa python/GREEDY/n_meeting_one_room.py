class Meeting:
    def __init__(self,s,e,p):
        self.s=s
        self.e=e
        self.p=p

class Solution:
    def maxMeetings(self, s, f):
        n=len(s)
        meet=[Meeting(s[i],f[i],i+1)for i in range(n)]
        meet.sort(key = lambda x:(x.e,x.p))
        res=[meet[0].p]
        last_time=meet[0].e
        for i in range(1,n):
            if meet[i].s>last_time:
                res.append(meet[i].p)
                last_time=meet[i].e
        return sorted(res)
    
s = [1, 3, 0, 5, 8, 5]
e = [2, 4, 6, 7, 9, 9] 
sol=Solution()
print(sol.maxMeetings(s,e))