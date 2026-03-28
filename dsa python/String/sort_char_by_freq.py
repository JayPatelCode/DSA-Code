s="tree"
n=len(s)
dct={}
res=""
for i in range(n):
    dct[s[i]]=dct.get(s[i],0)+1

sorted_val=sorted(dct.items(),key=lambda x:x[1],reverse=True)
print(sorted_val)
for val,freq in sorted_val:

    res=res+(val*freq)
# print(dct)
print(res)