nums = [3,2,3]
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

    if freq[num] > len(nums) // 2:
        print(num)