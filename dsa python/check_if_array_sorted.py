arr=[12, 35, 1, 10, 34, 1]
n=len(arr)
for i in range(n-1):
    if arr[i]>arr[i+1]:
        print(False)
print(True)