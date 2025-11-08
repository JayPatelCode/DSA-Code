capacity = [2,3,4,5]
rocks = [1,2,4,4]
additionalRocks = 2
# for i in range(len(capacity)):
#     max_val_added=capacity[i]
#     curr_val_capacity=rocks[i]
#     if curr_val_capacity<max_val_added:
#         if additionalRocks!=0:
#             curr_val_capacity+=1
#             additionalRocks-=1
        
#     print(capacity[i],rocks[i])
# print(rocks)

need=[capacity[i]-rocks[i] for i in range(len(rocks))]
need.sort()
print(need)
count=0
for n in need:
    if n==0:
        count+=1
    elif additionalRocks>=n:
        additionalRocks-=n
        count+=1
    else:
        break
