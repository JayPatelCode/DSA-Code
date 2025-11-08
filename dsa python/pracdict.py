# ans={}

# again=False
# while not again: 
#     name=input("Enter name: ")
#     price=int(input("Enter price: "))
#     ans[name]=price
#     inp=input("Do you want to insert more enter yes/no")
#     if inp == "no":
#         again=True
#         print(ans)
    


# nst=[1,2,3,4,[5,6,7,8]]
# print(nst[4][3])



################### Product except self #################
# lst=[1,2,3,4]
# ans=[]
# for i in range(len(lst)):
#     total=1
#     for j in range(len(lst)):
#         if i != j:
#             total*=lst[j]
#             print(total)
#     ans.append(total)
# print(ans)

################## OR ####################
# lst=[1,2,3,4]
# n = len(lst)
# ans = [1] * n
# for i in range(1,n):
#     ans[i] = ans[i-1] * lst[i-1]

# right_product= 1
# for i in range(n-1,-1,-1):
#     ans[i] = ans[i] * right_product

#     right_product = right_product * lst[i]

# print(ans)



# lst=[1,2,3,4,5,6,7,8]

# for i in range(len(lst)-1,-1,-1):
#     print(lst[i])


# x=10
# while x>=0:
#     print(x)
#     x-=1

fruits=["apple","banana","grapes"]
print(fruits[::-1])