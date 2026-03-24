# num=int(input("Enter number"))
# count=0
# while num:
#     num=num//10
#     count+=1

# print(count)




#######REV######3333
# num=int(input("Enter number"))
# rev=0
# while num:
#     last_num=num%10
#     num=num//10
#     rev=rev*10+last_num

# print(rev)




# from math import *

# num=int(input("Enter number"))
# print(int(log10(num)+1))




n=589
count=0
rev=0
while n:
    last=n%10
    # print(last)
    rev=rev*10+last
    print(rev,"REV")
    n=n//10
print(rev)