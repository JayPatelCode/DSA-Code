import heapq
stones = [2,7,4,1,8,1]
st=[-stone for stone in stones]
heapq.heapify(st)
print(st)
for st in stones:
    lt=heapq.heappop(st)
    rt=heapq.heappop(st)