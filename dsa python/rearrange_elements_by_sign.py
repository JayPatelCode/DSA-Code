


########I tried it but will not work for odd length###
# nums=[5,10,-3,-1,-10,6]
# n=len(nums)
# i=0
# j=n-1
# nlst=[]
# print(sorted(nums))
# nums=(sorted(nums))
# for i in range(n//2):
#     nlst.append(nums[i])
#     i+=2
#     nlst.append(nums[j])
#     j-=1
# print(nlst)

############This will work but we want in sequence not first last#######
# nums=[5,10,-3,-1,-10,6]
# n=len(nums)
# i=0
# j=n-1
# nlst=[]
# nums.sort()

# while i<=j:
#     if j==i:
#         nlst.append(nums[j])
#     else:
#         nlst.append(nums[i])
#         nlst.append(nums[j])
#     i+=1
#     j-=1
# print(nlst)



# ###############Brute appraoch#######
# nums=[3,1,-2,-5,2,-4]
# n=len(nums)
# pos=[]
# neg=[]

# for i in range(n):
#     if nums[i]>0:
#         pos.append(nums[i])
#     else:
#         neg.append(nums[i])

# pos_len=len(pos)
# neg_len=len(neg)
# i,j=0,0
# res=[]
# while i<pos_len and j<neg_len:
#     res.append(pos[i])
#     res.append(neg[j])
#     i+=1
#     j+=1

# while i<pos_len:
#     res.append(pos[i])
#     i+=1
# while j<neg_len:
#     res.append(neg[j])
#     j+=1
# print(res)



###############second Brute appraoch#######
# nums=[3,1,-2,-5,2,-4]
# n=len(nums)
# pos=[]
# neg=[]

# for i in range(n):
#     if nums[i]>0:
#         pos.append(nums[i])
#     else:
#         neg.append(nums[i])
# for i in range(len(pos)):
#     nums[2*i]=pos[i]
#     nums[(2*i)+1] = neg[i]
# print(nums)
    



##############Optimal appraoch#######
nums=[3,1,-2,-5,2,-4]
n=len(nums)
res=[0] * n
pos_ind=0
neg_ind=1
for i in range(n):
    if nums[i]>0:
        res[pos_ind]=nums[i]
        pos_ind+=2
    else:
        res[neg_ind]=nums[i]
        neg_ind+=2
    
print(res)