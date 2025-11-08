# nums = [4,1,2,3]
# res=[]
# even=[sev for sev in nums if sev%2==0]
# odd=[sod for sod in nums if sod%2==1]
# even_itr=0
# odd_itr=0
# even.sort()
# odd.sort(reverse=True)
# for i in range(len(nums)):
#     if nums[i]%2==0:
#         res.append(even[even_itr])
#         print(even[even_itr])
#         even_itr+=1
#     else:
#         res.append(odd[odd_itr])
#         odd_itr+=1
# print(res)





nums = [4,1,2,3]
res=[]
even=[nums[i] for i in range(0, len(nums), 2)]
odd=[nums[i] for i in range(1, len(nums), 2)] 
print(even,odd)
even_itr=0
odd_itr=0
even.sort()
odd.sort(reverse=True)
for i in range(len(nums)):
    if i%2==0:
        res.append(even[even_itr])
        print(even[even_itr])
        even_itr+=1
    else:
        res.append(odd[odd_itr])
        odd_itr+=1
print(res)