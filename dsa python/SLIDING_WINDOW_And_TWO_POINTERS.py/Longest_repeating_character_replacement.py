s = "ABAB"
k = 2
l=0
r=0
my_dict={}
maxi=0
n=len(s)
while r<n:
    my_dict[s[r]]=my_dict.get(s[r],0)+1
    if (r-l+1) - max(my_dict.values()) > k:
        my_dict[s[l]]-=1
        l+=1
    
    maxi=max(maxi,r-l+1)
    r+=1

print(maxi)
print(my_dict)