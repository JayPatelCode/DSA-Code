
matrix = [[1,2,3],[4,5,6],[7,8,9]]

############Brute force#######

# n=len(matrix)
# result=[[0 for _ in range(n)] for _ in range (n)] 
# for i in range(n):
#     for j in range(n):
#         result[j][(n-1)-i]=matrix[i][j]

# print(result)

# TC: O(n2)
# SC: O(n2)



##############OPTIMAL########
n=len(matrix)

for i in range(n-1):
    for j in range(i+1,n):
            matrix[i][j],matrix[j][i] =matrix[j][i],matrix[i][j]
print(matrix)

for i in range(n):
    matrix[i].reverse()

print(matrix)