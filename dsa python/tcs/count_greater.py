arr=[7,4,8,2,9]
# output=3                         7,8,9
n=len(arr)
m=float("-inf")
count=0
for i in range(n):
   if m<arr[i]:
        m=arr[i]
        count+=1  

print(count)