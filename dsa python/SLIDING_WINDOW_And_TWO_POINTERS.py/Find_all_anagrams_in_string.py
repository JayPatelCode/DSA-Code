s = "cbaebabacd"
p = "abc"


s_count={}
p_count={}
for i in range(len(p)):
    s_count[s[i]]=s_count.get(s[i],0)+1
    p_count[p[i]]=p_count.get(p[i],0)+1

res=[0] if p_count==s_count else []
l=0
for i in range(len(p),len(s)):
    s_count[s[i]]=s_count.get(s[i],0)+1

    s_count[s[l]]-=1
    if s_count[s[l]] == 0:
        del s_count[s[l]]

    l+=1

    if p_count==s_count:
        res.append(l)
print(res)



# print(s_count)
# print(p_count)