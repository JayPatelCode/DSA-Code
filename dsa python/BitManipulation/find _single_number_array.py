nums = [4,1,2,1,2]

#########BRUTE#######

# hsmp={}
# for i in range(len(nums)):
#     hsmp[nums[i]]=hsmp.get(nums[i],0)+1
# for k,v in hsmp.items():
#     if v==1:
#         print(k)
# print(hsmp)



a=0
for i in nums:
    a=a^i
print(a)