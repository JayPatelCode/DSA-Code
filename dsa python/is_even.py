
# def is_even(num):
#     if num%2==1:
#         return num+1
#     else:
#         return num
        
# x=[12,9,14,67,54,33,10]

# y=[]
# for num in x:
#     y.append(is_even(num)) 

# print(y)





#####or


def is_even(num):
    if num%2==1:
        return num+1
    else:
        return num
        
x=[12,9,14,67,54,33,10]

# y=list(map(is_even,x))   #map(function,iterable)

###or

y=[is_even(num) for num in x]
print(y)