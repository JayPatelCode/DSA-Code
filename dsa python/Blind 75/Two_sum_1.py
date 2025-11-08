from collections import Counter, defaultdict


# target=9
# nums=[2,8,11,1]
# ans=[]
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i] != nums[j] and nums[i] + nums[j] == target:
#             ans.append(nums[j])
#         else:
#             continue

# print(ans)


#############OR#########
# cnt={}
# for i,num in enumerate(nums):
#     diff=target-num
#     if diff in cnt:
#         print(cnt[diff],i)
#     cnt[num]=i


#############NOPE#########
# nums=[2,11,7,15]
# target=9
# hsmp={}
# for i in range(len(nums)):
#     diff= target-nums[i]
#     hsmp[nums[i]]=hsmp.get(nums[i],0)+1

# for n in hsmp:
#     diff= target-n
#     if diff in hsmp:
#         print(diff,n)
#         break


# nums=[2,11,7,15]
# target=9
# hsmp={}
# for i in range(len(nums)):
#     diff= target-nums[i]
#     if diff in hsmp:
#         print(hsmp[diff],i)
#         break
#     hsmp[nums[i]]=i
# print(hsmp)


nums=[2,11,7,15]
n=len(nums)
target=9
hsmp={}
for i in range(n):
    diff=target-nums[i]
    if diff in hsmp:
        print(hsmp[diff],i)
        break
    hsmp[nums[i]]=i










    