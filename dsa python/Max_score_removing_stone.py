a = 2 
b = 4
c = 6
stones=sorted([a,b,c])
x,y,z=stones
print(x,y,z)
if x+y<=z:
    print(x+y)
else:
    print((x+y+z)//2)