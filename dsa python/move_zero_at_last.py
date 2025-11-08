nums = [0,1,0,3,12]
n=len(nums)
temp=[]
for i in range(n):
    if nums[i]!=0:
        temp.append(nums[i])

n2=len(temp)
for i in range(n2):
    nums[i]=temp[i]

for i in range(n2,n):
    nums[i]=0
print(temp)
print(nums)






###########OPTIMAL######3
# nums = [0,1,0,3,12]
# i=0
# n=len(nums)
# for j in range(n):
#     if nums[j]!=0:
#         nums[i],nums[j]=nums[j],nums[i]
#         i+=1

# print(nums)