from collections import Counter
arr = [3,3,3,3,5,5,5,2,2,7]
freq={}
for i in range(len(arr)):
    freq[arr[i]]=freq.get(arr[i],0)+1
print(freq.values())
val=sorted(freq.values(),reverse=True)
print(freq)
print(val)

removed = 0
total_removed = 0
half = len(arr) // 2
for f in val:
    total_removed+=f
    removed+=1
    if total_removed >= half:
        break
print(removed)