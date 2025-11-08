#######SELECTION SORT ASC#######33333
# nums=[1,2,8,4,5,6,9,7]

# n=len(nums)
# for ind in range(0,n):
#     min_ind=ind
#     for j in range(ind+1,n):
#         if nums[j]<nums[min_ind]:
#             min_ind=j
#     nums[ind],nums[min_ind]=nums[min_ind],nums[ind]
# print(nums)



#######SELECTION SORT DESC#######33333
# nums=[1,2,8,4,5,6,9,7]

# n=len(nums)
# for i in range(n):
#     max_ind=i
#     for j in range(i+1,n):
#         if nums[j]>nums[max_ind]:
#             max_ind=j
#     nums[max_ind],nums[i]=nums[i],nums[max_ind]
# print(nums)

# TC: O(n2)
# SC: O(1)


# #######BUBBLE SORT DESC#######33333
# nums=[1,2,8,4,5,6,9,7]
# n=len(nums)
# for i in range(n-2,-1,-1):
#     for j in range(0,i+1):
#         if nums[j]<nums[j+1]:
#             nums[j],nums[j+1]=nums[j+1],nums[j]

# print(nums)


#######BUBBLE SORT ASC#######33333
# nums=[1,2,8,4,5,6,9,7]
# n=len(nums)
# for i in range(n):
#     for j in range(n-1-i):
#         if nums[j]>nums[j+1]:
#             nums[j],nums[j+1]=nums[j+1],nums[j]

# print(nums)


############insertion sort###
# nums=[40,30,20,10]
# n=len(nums)
# for i in range(1,n):
#     key=nums[i]
#     j=i-1
#     while j>=0 and key<nums[j]:
#         nums[j+1]=nums[j]
#         j-=1
#     nums[j+1]=key

# print(nums)

# Complexity
# Case	Time	Why
# Worst / Average	O(n²)	In reversed or random arrays, each new key may scan almost the whole sorted part.
# Best	O(n)	If the array is already sorted, the while test fails immediately every time.
# Space	O(1)	Sort happens in place; only a few variables (key, i, j).


########Merge sort#######

# def merge_arr(left,right):
#     result=[]
#     i,j=0,0
#     n=len(left)
#     m=len(right)
#     while i<n and j<m:
#         if left[i]<right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#     if i<n:
#         result.extend(left[i:])
#     else:
#         result.extend(right[j:])
#     return result

# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     mid=len(arr)//2
#     left_arr=arr[:mid]
#     right_arr=arr[mid:]
#     left=merge_sort(left_arr)
#     right=merge_sort(right_arr)
#     return merge_arr(left,right)

# nums=[3,1,2,4,1,5,2,6,4]
# print(merge_sort(nums))

# TC:O(nlog⁡n)
# SC: O(n)


#######Quick sort#########

def partition(nums,low,high):
    pivot=nums[low]
    i=low
    j=high
    while i<j:
        while i <= high-1 and nums[i] <= pivot:
            i += 1
        while j >= low+1 and nums[j] > pivot:
            j -= 1

        if i<j:
            nums[i],nums[j]=nums[j],nums[i]

    nums[low],nums[j]=nums[j],nums[low]
    return j


def quick_sort(nums,low,high):
    if low<high:
        p_index=partition(nums,low,high)
        quick_sort(nums,low,p_index-1)
        quick_sort(nums,p_index+1,high)

nums = [3, 2, 6, 4, 1, 5]
n=len(nums)
quick_sort(nums,0,n-1)
print(nums)

# TC: O(nlogn)
# SC: O(n) 