# arr=[1,0,-1,0,-2,2,5,9]

# n=len(arr)
# if n<4:
#     print([])
# res=set()
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             for l in range(k+1,n):
#                 if arr[i]+arr[j]+arr[k]+arr[l]==0:
#                     temp=[arr[i],arr[j],arr[k],arr[l]]
#                     temp.sort()
#                     res.add(tuple(temp))
# print([list(ans) for ans in res])








# arr=[1,0,-1,0,-2,2,5,9]
# target=0
# n=len(arr)
# if n<4:
#     print([])
# res=set()
# for i in range(n):
#     for j in range(i+1,n):
#         st=set()
#         for k in range(j+1,n):
#             fourth=target-(arr[i]+arr[j]+arr[k])
#             if fourth in st:
#                 temp=[arr[i],arr[j],arr[k],fourth]
#                 temp.sort()
#                 res.add(tuple(temp))
#             st.add(arr[k])
# print([list(ans) for ans in res])





#########OPTIMAL######

arr=[1,0,-1,0,-2,2,5,9]
target=0
n=len(arr)
arr.sort()
res=[]

for i in range(n):
    if i>0 and arr[i-1]==arr[i]:
        continue
    for j in range(i+1,n):
        if j>i+1 and arr[j]==arr[j-1]:
            continue
        k=j+1
        l=n-1

        while k<l:
            total=arr[i]+arr[j]+arr[k]+arr[l]
            if total==target:
                res.append([arr[i],arr[j],arr[k],arr[l]])
                k+=1
                l-=1
                while k<l and arr[k-1]==arr[k]:
                    k+=1
                while l>k and arr[l]==arr[l+1]:
                    l-=1
            
            elif total>target:
                l-=1
            else:
                k+=1
    print(res)