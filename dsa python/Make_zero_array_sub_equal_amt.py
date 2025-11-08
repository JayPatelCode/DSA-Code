#############BETTER#########
nums = [1,5,0,3,5]
n=len(nums)
cnt=0
n=set(nums)
print(nums)
for i in n:
    if i==0:
        continue
    else:
        print(i)
        cnt+=1
        print(cnt)
print(cnt)






###########optimal########3

# return len(set(num for num in nums if num>0))