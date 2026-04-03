########rotate right by 1

# arr=[1,4,6,8,9,4,2]
# n=len(arr)
# last=arr[n-1]
# for i in range(n-1,0,-1):
#     arr[i]=arr[i-1]

# arr[0]=last
# print(arr)


#######rotate left by 1
# arr=[1,4,6,8,9,4,2]
# n=len(arr)
# first=arr[0]
# for i in range(n-1):
#     arr[i]=arr[i+1]

# arr[n-1]=first
# print(arr)







###rotate left using slicing
# arr=[1,4,6,8,9,4,2]
# n=len(arr)
# arr[:]=arr[1:n] + [arr[0]]
# print(arr)


###rotate right using slicing
# arr=[1,4,6,8,9,4,2]
# n=len(arr)
# arr=[arr[n-1]] + arr[0:n-1]
# print(arr)







# arr=[1,4,6,8,9,4,2]

# first=arr[-1]
# n=len(arr)
# print(arr[n-1])
# for i in range(n-1,0,-1):
#     arr[i]=arr[i-1]
# arr[0]=first    
# print(arr)

#########LR####
# arr=[1,4,6,8,9,4,2]

# last=arr[0]
# n=len(arr)
# print(arr[n-1])
# for i in range(n-1):
#     arr[i]=arr[i+1]
# arr[-1]=last 
# print(arr)






















# prc

# arr=[1,4,6,8,9,4,2]
# n=len(arr)
# for i in range(n-1,-1,-1):
#     print(arr[i])



###########Right Rot by 1

# arr=[1,4,6,8,9,4,2]

# n=len(arr)-1
# fst=arr[n]

# for i in range(n,-1,-1):
#     arr[i]=arr[i-1]
# arr[0]=fst
# print(arr)

#lr by 1
arr=[1,4,6,8,9,4,2]

n=len(arr)-1
lst=arr[0]

for i in range(n):
    arr[i]=arr[i+1]
arr[n]=lst
print(arr)




