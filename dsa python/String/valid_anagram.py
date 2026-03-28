s="anagram"
t="nagaram"
if len(s)!=len(t):
    return False
n=len(s)
dc={}
for i in range(n):
    dc[s[i]]=dc.get(s[i],0)+1

for i in t:
    if i not in dc:
        return False
    elif i in dc and dc[i]>0:
        dc[i]-=1
    
for val in dc.values():
    if val!=0:
        return False

return True