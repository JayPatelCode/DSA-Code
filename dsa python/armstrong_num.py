# def countnum(num):
#     count=0
#     while num!=0:
#         num=num//10
#         count+=1
#     return count
# num=int(input("Enter numer: "))
# k=countnum(num)
# sum=0
# temp=num
# while num>0:
#     digit=num%10
#     sum = sum+ digit**k
#     num=num//10
# print(temp==sum)    




num=int(input("Enter numer: "))
n=num
total=0
count=len(str(num))
while num>0:
    last_dig=num%10
    total=total+(last_dig**count)
    num=num//10
# print(total)
print(total==n)




