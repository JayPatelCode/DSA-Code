jewles = "aA"
stones = "aAAbbbb"
jewle_set=set(jewles)
print(jewle_set)
count=0
for stone in stones:
    if stone in jewle_set:
        count+=1

print(count) 