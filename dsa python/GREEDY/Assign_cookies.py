# greed=[2,6,8,1,4]
# s=[4,2,7,1,2,3]
# greed.sort()
# s.sort()
# n=len(greed)
# print(greed)
# print(s)
# i=0
# cnt=0

# for ind in range(n):
#     if s[ind]>=greed[ind]:
#         print(greed[ind],s[ind])
#         cnt+=1
# print(cnt)
    


greed=[2,6,8,1,4]
s=[4,2,7,1,2,3]
greed.sort()
s.sort()
n=len(greed)
m=len(s)
l=0
r=0
cnt=0

while l<n and r<m:
    if s[r]>=greed[l]:
        cnt+=1
        l+=1
    r+=1
print(cnt)
    
