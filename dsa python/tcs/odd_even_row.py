matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result=[]
for i,row in enumerate(matrix):
    if i%2==0:
        result.append(row)
    else:
        result.append(row[::-1])

print(result)