arr = [0,2,1,5,3,4]
n=len(arr)
nums=[]
for i in range(len(arr)):
    nums.append(arr[arr[i]])
print(nums)