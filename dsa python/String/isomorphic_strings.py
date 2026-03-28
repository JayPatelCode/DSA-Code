# s="paperpe"
# t="titlesl"

s = "egg"
t = "add"
n=len(s)
map_store={}
map_cont=set()
for i in range(n):

    if s[i] in map_store:
        
        if map_store[s[i]]==t[i]:
            continue
        else:
            print("Its wrong value")
            break
    else:
        if t[i] in map_cont:
            print(False)
            break
        map_store[s[i]]=t[i]
        map_cont.add(t[i])
print(map_store)