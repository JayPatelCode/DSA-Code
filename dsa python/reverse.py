from collections import defaultdict

num=int(input("Enter number"))
reversed_num=0
while num:
    digit=num%10                 
    reversed_num=reversed_num*10+digit
    num=num//10               


print(reversed_num) 


##########LIST COMP###33333
# num=int(input("Enter number"))
# n=[i*i if i%2==0 else i*i*i for i in range(11)]
# print(n)


#############Count characters######3

# str="abcabcb"
# cnt=defaultdict(int)
# print(cnt)

# for i in str:
#     print(cnt[i])
#     cnt[i]+=1

# print(cnt)




########reverse string######
# str1 = "P@#yn26at^&i5ve"
# str=""
# for c in str1:
#     print(c)
#     str=c+str
# print(str)