###############BRUTE FORCE###########

# prices=[7,2,1,5,6,4,8]
# n=len(prices)
# max_prof=0
# for b in range(n):
#     for s in range(b+1,n):
#         if prices[s]>prices[b] :
#             prof=prices[s]-prices[b]
#             max_prof=max(prof,max_prof)

# print(max_prof)







######Optimised#######
prices=[7,2,1,5,6,4,8]
n=len(prices)
max_prof=0
min_prof=float("inf")

for i in range(n):
    min_prof=min(min_prof,prices[i])
    max_prof=max(max_prof,prices[i]-min_prof)

print(max_prof)
