arr=[12, 35, 1, 10, 34, 1]
max,sec = float('-inf'),float('-inf')
for i in arr:
    if i>max:
        sec=max
        max=i
    elif i<max and i>sec:
        sec=i
if sec==float('-inf'):
    print(-1)
else:
    print(sec)