nums1=[1,1,1,2,4,6,7]
nums2=[1,2,3,6,7,8,9,10]
res=[]
n1=len(nums1)
n2=len(nums2)
i,j=0,0

while i<n1 and j<n2:
    if nums1[i]<nums2[j]:
        res.append(nums1[i])
        i+=1
    else:
        res.append(nums2[j])
        j+=1

res.extend(nums1[i:])
res.extend(nums2[j:])
print(res)


