# lst= list(map(int,input().split()))
# n=len(lst)

# for i in range(n//2):
#     lst[i],lst[n-1-i] = lst[n-1-i],lst[i]

# print(lst)





############# OR




lst= list(map(int,input().split()))
n=len(lst)

s=0
e=n-1
while s<=e:
    lst[s],lst[e]=lst[e],lst[s]
    s+=1
    e-=1
print(lst)