arr= [2, 3, 2, 3, 5]
res=[]
dct={}
for i in range(len(arr)):
    dct[arr[i]]=dct.get(arr[i],0)+1

# print(dct)

for i in range(1,len(arr)+1):
    if i in dct:
        res.append(dct[i])
    else:
        res.append(0)
print(res)