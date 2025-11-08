######brute force#####3
# arr=[1, 1, 1, 2,2,3,4,4,4,5,5]
# dct={}
# n=len(arr)
# for i in range(n):
#     dct[arr[i]]=0
# j=0
# for k in dct:
#     arr[j]=k
#     j+=1
# print(dct)
# print(j)
# print(arr)






arr=[1, 1, 1, 2,2,3,4,4,4,5,5]
i=0
j=i+1
n=len(arr)
if n==1:
    print(1)
while j<n:
    if arr[i]!=arr[j]:
        i+=1
        arr[i],arr[j]=arr[j],arr[i]
    j+=1
    
print(i+1)
print(arr)