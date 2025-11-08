##################Brute###########

# arr=[-1,0,1,2,-1,-4]
# n=len(arr)
# st=set()
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if arr[i]+arr[j]+arr[k]==0:
#                 temp=[arr[i],arr[j],arr[k]]
#                 temp.sort()
#                 st.add(tuple(temp))

# print([list(ans) for ans in st])








##########Better#######33

# arr=[-1,0,1,2,-1,-4]
# n=len(arr)
# result=set()
# for i in range(n):
#     st=set()
#     for j in range(i+1,n):
#         k=-(arr[i]+arr[j])
#         if k in st:
#             temp=[arr[i],arr[j],k]
#             temp.sort()
#             result.add(tuple(temp))
#         st.add(arr[j])
# print([list(ans) for ans in result])





from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result=[]
        nums.sort()
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue

            j=i+1
            k=n-1

            while j<k:
                total_sum=nums[i]+nums[j]+nums[k]
                if total_sum<0:
                    j+=1
                elif total_sum>0:
                    k-=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    result.append(temp)
                    j+=1
                    k-=1

                    while j<k and nums[j]==nums[j-1]:
                        j+=1

                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return result