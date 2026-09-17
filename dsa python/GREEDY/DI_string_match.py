s = "IDID"

n = len(s)
left = 0
right = n
res = []

for char in s:
    if char == "I":
        res.append(left)
        left += 1
    else:
        res.append(right)
        right -= 1

res.append(right)

print(res)
