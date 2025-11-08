# num=int(input("Enter numer: "))
# lis=[]
# for i in range(1,num+1):
#     if num%i==0:
#         lis.append(i)
# print(lis)


# or


# num=int(input("Enter numer: "))
# k=1
# while k*k<=num:  
#     if num %k==0:     
#         print(k)
#         if k !=(num//k):    
#             print(num//k)
#     k+=1
    










# ORRRRRRRRRRRRRRRRRRRRR

# num=int(input("Enter numer: "))
# lst=[]
# for i in range(1,num+1):
#     if num%i==0:
#         lst.append(i)
# print(lst)

# TC O(N)
# SC O(K) where k is total no of factors



####OPTIMIZED
from math import sqrt


num=int(input("Enter numer: "))
lst=[]
for i in range(1,int(sqrt(num)+1)):
    if num%i==0:
        lst.append(i)
        if num//i != i:
            lst.append(num//i)

print(sorted(lst))

# TC O(sqrt(N)) + O(NlogN)
# SC O(K) where k is total no of factors






# num=int(input("Enter numer: "))
# lst=[]
# for i in range(1,num//2+1):
#     if num%i==0:
#         lst.append(i)

# lst.append(num)
# print(lst)