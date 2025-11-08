# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"

word1 = "abc"
word2 = "pqr"
i,j=0,0
merged=""
a=len(word1)
b=len(word2)

while i<a and j<b:
    merged += word1[i]+word2[j]
    i+=1
    j+=1

if i<a:
    merged += word1[i:]
else:
     merged += word2[j:]
print(merged)