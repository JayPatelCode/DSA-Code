nums = [0,1,1,1,1,1,0,0,0]

count = 0
max_len = 0
prefix_map = {0: -1}  # sum -> first index

for i, num in enumerate(nums):
    # convert 0 to -1
    count += 1 if num == 1 else -1

    if count in prefix_map:
        max_len = max(max_len, i - prefix_map[count])
    else:
        prefix_map[count] = i

print(max_len)