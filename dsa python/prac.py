# channels: list[str] = ['Hello','lost',"agree",'beel' ]

# for i, channel in enumerate(channels):
#     if channel == 'lost':
#         channels.remove(channel)
#     print(i,channel)



# rev = [3,2,5,1,4,9]
# r=[]
# for reversed in reversed(rev):
#     r.append(reversed)
# print(r)


# rev = [3,2,5,1,4,9]
# r = rev[::-1]
# print(r)


# rev = [3,2,5,1,4,9]

# a=0
# b=len(rev)-1
# while a < b:
#     rev[a],rev[b]=rev[b],rev[a]
#     a += 1
#     b -= 1
# print(rev)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result=[]
for list in matrix:
    for i in list:
        result.append(i)

print(result)


mat=[i for list in matrix for i in list]
print(mat)