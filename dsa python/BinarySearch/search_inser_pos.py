nums=[2,4,6,7,9,11,18,19]
n=len(nums)
target=8
low=0
high=n-1
lb=n
while low<=high:
    mid=(low+high)//2
    if nums[mid]>=target:
        high=mid-1
        lb=mid
    else:
        low=mid+1
print(lb)