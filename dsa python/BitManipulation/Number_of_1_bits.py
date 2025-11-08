############Its also called hamming weight#########
n = 11
# Output: 3
ans=0
while n!=0:
    ans+=1
    n=n&(n-1)
print(ans)