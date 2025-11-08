###########Brute########
# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
# n=len(nums)
# maxi=0
# for i in range(n):
#     zeros=0
#     for j in range(i,n):
#         if nums[j]==0:
#             zeros+=1
#         if zeros>k:
#             break
#         maxi=max(maxi,j-i+1)
# print(maxi)



# ########Better###########
# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
# n=len(nums)
# r=0
# l=0
# maxi=0
# zeros=0
# while r<n:
#     if nums[r]==0:
#         zeros+=1
#     while zeros>k:
#         if nums[l]==0:
#             zeros-=1
#         l+=1
    
#     if zeros<=k:
#         maxi=max(maxi,r-l+1)
#         r+=1
# print(maxi)



######optimal######
########Better###########
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
n=len(nums)
r=0
l=0
maxi=0
zeros=0
while r<n:
    if nums[r]==0:
        zeros+=1
    if zeros>k:
        if nums[l]==0:
            zeros-=1
        l+=1
    
    if zeros<=k:
        maxi=max(maxi,r-l+1)
    r+=1
print(maxi)