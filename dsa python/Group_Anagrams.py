from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
result=[]
hsmp=defaultdict(list)
for s in strs:
    srt=tuple(sorted(s))
    hsmp[srt].append(s)

for k in hsmp:
    result.append(hsmp[k])

print(result)