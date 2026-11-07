accounts = [[1,2,3],[3,2,1]]
r=len(accounts)
c=len(accounts[0])

max_wealth = 0
for acc in accounts:
    sum = 0
    for j in acc:
        sum +=j
    max_wealth = max(max_wealth,sum)
print(max_wealth)