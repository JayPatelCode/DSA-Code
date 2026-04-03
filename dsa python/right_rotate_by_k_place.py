
# Koutetsu no Majo Annerose 1
# Milfty - Krystal Sparks
# Pure Mature - Kyle Mason - Justine Jakobs - Thrill The Messenger / 03.03.2025
# Pure Mature - Alix Lynx - Double "Ohhh" Danger / 29.05.2023
# ###############Right rotate by k place######
# arr=[1,4,6,8,9,4,2]
# n=len(arr)
# a=int(input("Enter by how many place you want to rotate array by right: "))

# for i in range(a):
#     f_num=arr.pop()
#     arr.insert(0,f_num)
# print(arr)



# ###############Right rotate by k place######
# arr=[1,4,6,8,9,4,2]
# n=len(arr)
# a=int(input("Enter by how many place you want to rotate array by right: "))
# right_rotations=a%n
# for i in range(right_rotations):
#     f_num=arr.pop()
#     arr.insert(0,f_num)
# print(arr)





# ###############left rotate by k place######
# arr=[1,4,6,8,9,4,2]
# n=len(arr)
# a=int(input("Enter by how many place you want to rotate array by left: "))

# for i in range(a):
#     f_num=arr.pop(0)
#     arr.insert(n-1,f_num)
# print(arr)






###############left rotate by k place######
# arr=[1,4,6,8,9,4,2]
# n=len(arr)
# a=int(input("Enter by how many place you want to rotate array by left: "))
# left_rotations=a%n
# for i in range(left_rotations):
#     f_num=arr.pop(0)
#     arr.insert(n-1,f_num)
# print(arr)














###########Better approach####

###############Right rotate by k place######
# arr=[1,4,6,8,9,4,2]
# n=len(arr)
# a=int(input("Enter by how many place you want to rotate array by right: "))
# arr[:]=arr[n-a:] + arr[0:n-a]
# print(arr)


###############Left rotate by k place######

# arr=[1,4,6,8,9,4,2]
# n=len(arr)
# a=int(input("Enter by how many place you want to rotate array by left: "))
# a=a%n
# arr[:]=arr[a:] + arr[0:a]
# print(arr)








###########Optimal approach####

# ###############Right rotate by k place######
# arr=[1,4,6,8,9,4,2]
# n=len(arr)

# def reverse(nums,left,right):
#     while left<right:
#         nums[left],nums[right]=nums[right],nums[left]
#         left+=1
#         right-=1

# arr=[1,4,6,8,9,4,2]
# n=len(arr)
# a=int(input("Enter by how many place you want to rotate array by right: "))
# reverse(arr,n-a,n-1)
# reverse(arr,0,n-a-1)
# reverse(arr,0,n-1)

# print(arr)





###############Right rotate by k place######
# arr=[1,4,6,8,9,4,2]
# n=len(arr)

# def reverse(nums,left,right):
#     while left<right:
#         nums[left],nums[right]=nums[right],nums[left]
#         left+=1
#         right-=1

# arr=[1,4,6,8,9,4,2]
# n=len(arr)
# a=int(input("Enter by how many place you want to rotate array by left: "))
# reverse(arr,0,a-1)
# reverse(arr,a,n-1)
# reverse(arr,0,n-1)

# print(arr)


###############Right rotate by k place######
# arr=[1,4,6,8,9,4,2]
# n=len(arr)
# k=int(input("Enter value till you want to rotate: "))
# for i in range(k):
#     first_app=arr.pop()
#     arr.insert(0,first_app)
# print(arr)




###############Left rotate by k place######
# arr=[1,4,6,8,9,4,2]
# n=len(arr)
# k=int(input("Enter value till you want to rotate: "))
# for i in range(k):
#     last_app=arr.pop(0)
#     arr.insert(n-1,last_app)
# print(arr)







arr=[1,4,6,8,9,4,2]
n=len(arr)-1
a=int(input("Enter by how many place you want to rotate array by left: "))

arr[:]=arr[a:]+arr[0:a]
print(arr)