nums = [4,1,2,1,2]
hsmp={}
for i in range(len(nums)):
    hsmp[nums[i]]=hsmp.get(nums[i],0)+1

for k,v in hsmp.items():
    # print(i)
    if v==1:
        print(k)
# print(hsmp)