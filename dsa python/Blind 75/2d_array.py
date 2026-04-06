# nums=[[5,20,3],[4,3,7],[2,1,4]]
# rows=len(nums)
# cols=len(nums[0])
# sum=0
# for i in nums:
#     for j in i:
#         sum+=j
# print(sum)
# print(cols)






# nums=[[5,20,3],[4,3,7],[2,1,4]]
# rows=len(nums)
# cols=len(nums[0])
# for i in range(rows):
#     for j in range(cols):
#         print(nums[i][j],end=" ")
#     print()




# ###################PRINT upper triangle#####
# nums=[[5,2,3],[4,3,7],[2,1,4]]
# rows=len(nums)
# cols=len(nums[0])
# for i in range(rows):
#     for j in range(cols):
#         if j>=i:
#             print(nums[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()


####################PRINT lower triangle#####
# nums=[[5,20,3],[4,3,7],[2,1,4]]
# rows=len(nums)
# cols=len(nums[0])
# for i in range(rows):
#     for j in range(cols):
#         if i>=j:
#             print(nums[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()



# ####################PRINT diagonal#####
# nums=[[5,20,3],[4,3,7],[2,1,4]]
# rows=len(nums)
# cols=len(nums[0])
# for i in range(rows):
#     for j in range(cols):
#         if i==j:
#             print(nums[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()


# ####################PRINT diagonal#####
# nums=[[5,20,3],[4,3,7],[2,1,4]]
# rows=len(nums)
# n=len(nums)
# cols=len(nums[0])
# for i in range(rows):
#     for j in range(cols):
#         if (i+j==n-1):
#             print(nums[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()




# ####################PRINT transpose#####
# nums=[[5,9,1],[2,3,7]]
nums=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(nums)
n=len(nums)
cols=len(nums[0])
result=[[0]*rows for _ in range(cols)] 
print(result)
for i in range(rows):
    for j in range(cols):
        result[i][j]=nums[j][i]

print(result)


# nums=[[1,2,3],[4,5,6],[7,8,9]]
# n=len(nums)
# rows=n
# cols=len(nums[0])
# print(rows,cols)
# result=[[0]*rows for i in range(cols)]
# print(result)
# for i in range(rows):
#     for j in range(cols):
#         result[j][i]=nums[i][j]
# print(result)