# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


nums = [1,2,3,4]
ans = len(nums) * [1]
for i in range(1, len(nums)):
    ans[i] = ans[i-1] * nums[i-1]
    print(ans[i], nums[i-1])
