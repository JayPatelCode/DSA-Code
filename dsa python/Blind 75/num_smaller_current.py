# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
nums = [8,1,2,2,3]
srt=sorted(nums)
d={}
res=[]
for i,num in enumerate(srt):
    if num not in d:
        d[num]=i

for i in nums:
    res.append(d[i])

print(res)