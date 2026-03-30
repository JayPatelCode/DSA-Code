nums = [3,4,5,1,2]
n=len(nums)
l=0
h=n-1
mini=float("inf")
while l<=h:
    mid=(l+h)//2
    if nums[mid]<=nums[h]:
        if nums[mid]<=mini<=nums[h]:
            mini=nums[mid]
            l=mid+1

        else:
            h=mid-1

print(mini)

