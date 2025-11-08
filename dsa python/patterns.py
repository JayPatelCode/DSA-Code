# 5 4 3 2 1 
# 5 4 3 2 
# 5 4 3 
# 5 4 
# 5 

# n=6
# for i in range(1,n):
#     for j in range(1,n-i+1):
#         print(n-j, end=" ")
#     print()


#########ORRRRRRRRRRRRRRRRRR#############
# n=5
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()



#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

# n=6
# for i in range(1,n):

#     for j in range(1,n-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*", end=" ")
    
#     print()



# ******
# *****
# ****
# ***
# **
# *

# n=6
# for i in range(0,n):

#     for j in range(n-i):
#         print("*",end="")
    
#     print()





# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 


# n=5
# for i in range(0,n):

#     for k in range(i):
#         print(" ", end="")
    
#     for j in range(n-i):
#         print("*",end=" ")

    
#     print()




# * * * * * * * * * 
#  * * * * * * * 
#   * * * * * 
#    * * * 
#     * 



# n=5
# for i in range(n):

#     for k in range(i):
#         print(" ", end="")
    
#     for j in range(2*(n-i)-1):
#         print("*",end=" ")

    
#     print()


#     * 
#    * * * 
#   * * * * * 
#  * * * * * * * 
# * * * * * * * * * 

# n=5
# for i in range(n):

#     for j in range(n-i-1):
#         print(" ", end="")
    
#     for j in range((2*i)+1):
#         print("*",end=" ")
#     print()


# * * * * 
#  * * * 
#   * * 
#    * 

# n=4
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(n-i):
#         print("*", end=" ")
#     print()



#     * 
#    * * 
#   * * * 
#  * * * * *
#   * * * 
#    * * 
#     * 


# n=4
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()


# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*", end=" ")
#     print()





# * * * * 
#  * * * 
#   * * 
#    * 
# n=4
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end=" ")
#     print()



# n=5
# for i in range(n):
#     for j in range(n-i,0,-1):
#         print(j,end="")
#     print()








# n=4
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end=" ")
#     print()


#     *
#    ***
#   *****
#  *******
# *********


# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end="")
#     for j in range((2*(i))+1):
#         print("*", end="")
#     print()


# *********
#  *******
#   *****
#    ***
#     *


# n=5
# for i in range(n):

#     for j in range(i):
#         print(" ", end="")
#     for j in range((2*(n-i-1))+1):
#         print("*", end="")
#     print()







# n=5
# for i in range(n-1):
#     for j in range(n-i-1):
#         print(" ", end="")
#     for j in range((2*(i))+1):
#         print("*", end="")
#     print()

# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for j in range((2*(n-i-1))+1):
#         print("*", end="")
#     print()


a=int(input("Enter value of n: "))

for i in range(a):
    for j in range(a-i):
        print(a-i,end="")
    print()