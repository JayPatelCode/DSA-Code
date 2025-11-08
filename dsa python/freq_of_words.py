n=input("Enter the string: ")
l=n.split()
d={}
for w in l:
    d[w]=d.get(w,0)+1

print(d)