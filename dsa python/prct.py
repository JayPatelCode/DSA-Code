# data = {'banana': 3, 'apple': 1, 'cherry': 5, 'date': 2, 'elderberry': 4}
# srt=dict(sorted(data.items()))
# # print(srt)
# # print(data.items())
# # print(data.values())
# # for i in data.items():
# #     print(i)
# print(dict(sorted(data.items())))
# val=dict(sorted(data.items(),key=lambda x:x[1]))
# print(val)

# # Create list of squares of even numbers from 1-10
# print([x*x  for x in range(11) if x%2==0])







matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(matrix[0][2])
# for row in matrix:
#     print(row)

# for i in range(len(matrix)):
#     for j in range(len(matrix[1])):
#         print(matrix[i][j],end=" ")
#     print()



# row=2
# col=4
# # matrix=[[0 for _ in range(col)] for _ in range(row)]
# matrix = [[1 for _ in range(col)] for _ in range(row)]

# print(matrix)





# for row in matrix:
#     for val in row:
#         print(val, end=" ")
#     print()


# count = 0
# for row in matrix:
#     count += len(row)
#     print(count)
# # print(count)


for col in range(len(matrix[0])):
    col_sum = 0
    for row in range(len(matrix)):
        row_sum=0
        col_sum += matrix[row][col]
        row_sum += matrix[row][col]
        print(row_sum)
    # print(col_sum)

