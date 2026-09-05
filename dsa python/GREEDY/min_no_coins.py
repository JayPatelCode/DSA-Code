coins = [1,2,5]
amount = 11
lst=[]
n=len(coins)
for i in range(n-1,-1,-1):
    while amount>=coins[i]:

        lst.append(coins[i])
        amount-=coins[i]
print(lst)