
#################Brute#########
# nums = [4,5,6,7,0,1,2]
# target=1
# for i in range(len(nums)):
#     if nums[i]==target:
#         print(i)


nums = [4,5,6,7,0,1,2]
target=1
n=len(nums)
l=0
h=n-1
while l<=h:
    m=(l+h)//2
    if nums[m]==target:
        print(m)
        break
    elif nums[m]<=nums[h]:
        if nums[m]<=target<=nums[h]:     # target lies from mid to high  (sorted one)
            l=m+1
        else:
            h=m-1
    else:
        if nums[m]>=target>=nums[l]:       # target lies from low to mid
            h=m-1
        else:
            l=m+1
print(-1)