pattern = "abba"
s = "dog cat cat dog"
len_words=s.split()
if len(len_words)!=len(pattern):
    print(False)

c_to_w={}
w_to_c={}

for c,w in zip(pattern,len_words):
    if c in c_to_w:
        if c_to_w[c]!=w:
            print(False)
    else:
        c_to_w[c]=w


    if w in w_to_c:
        if w_to_c[w]!=c:
            print(False)
    else:
        w_to_c[w]=c
print(True)