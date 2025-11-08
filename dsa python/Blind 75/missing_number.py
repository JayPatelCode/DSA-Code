###########BRUTE###########

nums=[1,0]
n=len(nums)
for i in range(n+1):
    if i not in nums:
        print(i)


###########Better###########

nums=[1,0]
n=len(nums)
dct={}
for i in range(n+1):
    dct[i]=0

for i in nums:
    dct[i]=1

for i in dct:
    if dct[i]==0:
        print(i)
        
##############OPTIMAL######3
# nums=[1,0]
# print(sum(range(len(nums)+1)) - sum(nums))

