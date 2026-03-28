strs = ["flower","flow","flowing"]
base=strs[0]
str=""
for i in range(len(base)):
    for word in strs[1:]:
        if i==len(word) or word[i]!=base[i]:
            print(str)
            exit()
    str+=base[i]
print(str)
