s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(len(s))
seen=set()
repeated=set()

for i in range(len(s)-9):
    st=s[i:i+10]

    if st in seen:
        repeated.add(st)
    else:
        seen.add(st)

print(list(repeated))