# num=int(input("Enter numer: "))
# def pr(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# print(pr(num))




# or

# num=int(input("Enter numer: "))
# def pr(num):
#     i=2
#     while i*i<=num:
#         if num%i==0:
#             return False
#     return True
# print(pr(num))


# num=int(input("Enter numer: "))
# def pr(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# print(pr(num))


from math import sqrt

def prime(num):
    if num<2:
        return False
    for i in range(2,int(sqrt(num))+1):
        if num%i==0:
            return False
    return True

num=int(input("Enter numer: "))
print(prime(num))