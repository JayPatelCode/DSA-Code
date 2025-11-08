
nums=[1,1,0,1,1,1,1,0,1,1]
n=len(nums)
cnt=0
max_Count=0
for i in range(n):
    if nums[i]==1:
        cnt+=1
    else:
        max_Count=max(cnt,max_Count)
        cnt=0
max_Count = max(cnt, max_Count)
print(max_Count)

# Tc:O(N)
# Sc:O(1)