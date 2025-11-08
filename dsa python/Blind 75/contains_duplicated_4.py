from collections import defaultdict


# nums=[1,2,3,1]
# counter=defaultdict(int)

# for n in nums:
#     counter[n]+=1

# for c in counter:
#     if counter[c]>=2:
#         print("false")
# print("true")

# print(counter)




# counter=defaultdict(int)

# for n in nums:
#     counter[n]+=1

# for c in counter:
#     if counter[c]>=2:
#         return(True)
# return(False)







nums=[1,2,7]
count = {}
for i in nums:
    count[i]=count.get(i,0)+1
for c in count:
    if count[c]>=2:
        print("contains duplicates")