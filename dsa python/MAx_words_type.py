# text = "leet code"
# brokenLetters = "e"
# words=text.split()
# print(words)
# cnt=0
# for word in range(len(words)):
#     print(words[word])
#     if  brokenLetters[word]in words[word]:
#         continue
#     else:
#         cnt+=1
# print(cnt)





text = "leet code"
brokenLetters = "e"
words=text.split()
print(words)
cnt=0
for word in words:
    if  any(letter in word for letter in brokenLetters):
        continue
    else:
        cnt+=1
print(cnt)