from collections import defaultdict
magazine = "aab"
ransomNote = "aa"
counter=defaultdict(int)

for c in magazine:
    counter[c]+=1
    
for c in ransomNote:
    if c not in counter:
        print("False")
    elif counter[c]==1:
        del counter[c]
    else:
        counter[c]-=1

print("true")