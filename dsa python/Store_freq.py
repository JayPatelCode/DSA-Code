# from collections import defaultdict
# nums=[5,6,7,7,1,9,111,1,1,5,1,1]
# count=defaultdict(int)
# print(count)

# for i in nums:
#     count[i]+=1
# print(count)



########ORRRR


# nums=[5,6,7,7,1,9,111,1,1,5,1,1]
# x=1
# dct={}

# for i in range(len(nums)):
#     if nums[i] in dct:
#         dct[nums[i]]+=1
#     else:
#         dct[nums[i]]=1
# print(dct[x])



#############ORRR
# nums=[5,6,7,7,1,9,111,1,1,5,1,1]
# dct={}
# for i in range(len(nums)):
#     # print(i)
#     dct[nums[i]]=dct.get(nums[i],0)+1
#     print(dct[nums[i]])
# print(dct)

#############ORRR
# nums=[5,6,7,7,1,9,111,1,1,5,1,1]
# dct={}
# for i in nums:
#     # print(i)
#     dct[i]=dct.get(i,0)+1
#     print(dct[i])
# print(dct)
# Q1

# from collections import defaultdict
# n=[5,3,2,2,1]
# m=[10,111,1,9,5,67,2]
# cnt=defaultdict(int)
# for i in m:
#     for j in n:
#         if j == i:
#             cnt[j]+=1
# print(cnt)

###ORRRRR

# from collections import defaultdict
# n=[5,3,2,2,1]
# m=[10,111,1,9,5,67,2]
# for i in m:
#     cnt=0
#     for j in n:
#         if j == i:
#             cnt+=1
#     print(cnt)

########ORR
# from collections import defaultdict
# n=[5,3,2,2,1]
# m=[10,111,1,9,5,67,2]
# cnt=defaultdict(int)
# for i in n:
#     if i in m:
#         cnt[i]+=1
# print(cnt)
    


################OPTIMAL HASH map####333333
# n=[5,3,2,2,1]
# m=[10,111,1,9,5,67,2]
# hsmap=[0]*11
# for i in n:
#     hsmap[i]+=1
# for n in m:
#     if n<0 or n>10:
#         print(0)
#     else:
#         print(hsmap[n])

# TC: O(N+M)
# SC: O(1)    






# n=[5,3,2,2,1]
# m=[10,111,1,9,5,67,2]
# dct={}
# for i in n:
#     dct[i]=dct.get(i,0)+1
# for n in m:
#     if n<0 or n>10:
#         print(0)
#     else:
#         print(dct.get(n, 0))

# n=[5,3,2,2,1]
# m=[10,111,1,9,5,67,2]
# dct={}
# for i in range(len(n)):
#     dct[n[i]]=dct.get(n[i],0)+1
# print(dct, "DCT")
# for num in range(len(m)):
#     if m[num]<0 or m[num]>10:
#         print(0)
#     else:
#         print(dct.get(m[num], 0))


#########CHARACTER HASHING

s="azyxyyzaaaa"
q=["d","a","y","x"]
dct={}
for i in s:
    dct[i]=dct.get(i,0)+1
for d in q:
    print(dct.get(d, 0))