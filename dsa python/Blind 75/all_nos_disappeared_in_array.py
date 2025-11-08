nums = [4,3,2,7,8,2,3,1]
# nums = [1,1]
st=set(nums)
res=[]
for i in range(1,len(nums)+1):
    if i not in st:
        res.append(i)
print(res)