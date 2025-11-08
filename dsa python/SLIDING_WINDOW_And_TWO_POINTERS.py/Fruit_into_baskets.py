#######BRUTE#######

# fruits = [1,2,3,2,2]
# n=len(fruits)
# max_len=0
# for i in range(n):
#     my_set=set()
#     for j in range(i,n):
#         my_set.add(fruits[j])
#         if len(my_set)>2:
#             break

#     max_len=max(max_len,j-i+1)
# print(max_len)



#####BETTER####

# fruits = [1,2,3,2,2]
# n=len(fruits)
# max_len=0

# my_dict={}
# r=0
# l=0
# while r<n:
#     my_dict[fruits[r]]=my_dict.get(fruits[r],0)+1

#     while len(my_dict)>2:
#         my_dict[fruits[l]]-=1
#         if my_dict[fruits[l]]==0:
#             del my_dict[fruits[l]]
#         l+=1

#     if len(my_dict)<=2:
#         max_len=max(max_len,r-l+1)
#     r+=1
# print(max_len)




#####OPTIMAL####

fruits = [1,2,3,2,2]
n=len(fruits)
max_len=0

my_dict={}
r=0
l=0
while r<n:
    my_dict[fruits[r]]=my_dict.get(fruits[r],0)+1

    if len(my_dict)>2:
        my_dict[fruits[l]]-=1
        if my_dict[fruits[l]]==0:
            del my_dict[fruits[l]]
        l+=1

    if len(my_dict)<=2:
        max_len=max(max_len,r-l+1)
    r+=1
print(max_len)