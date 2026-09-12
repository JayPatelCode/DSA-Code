class Meeting:
    def __init__(self,s,e,p):
        self.s=s
        self.e=e
        self.p=p
        
class Solution:
    def activitySelection(self, start: list[int], finish: list[int]) -> int:
        n=len(start)
        meet=[Meeting(start[i],finish[i],i+1) for i in range(n)]
        meet.sort(key=lambda x:(x.e,x.s))
        last_time=meet[0].e
        count=1
        for i in range(1,n):
            if meet[i].s>last_time:
                count+=1
                last_time=meet[i].e
        return count