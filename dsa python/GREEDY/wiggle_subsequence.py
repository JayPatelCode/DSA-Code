class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        count = 1
        prev_diff = 0

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]

            if diff > 0 and prev_diff <= 0:
                count += 1
                prev_diff = diff

            elif diff < 0 and prev_diff >= 0:
                count += 1
                prev_diff = diff

        return count