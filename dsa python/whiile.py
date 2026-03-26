############product######33

# n=1
# prod=1
# while n<=3:
#     prod=prod*n
#     n+=1
# print(prod)



###########Reverse each word####3

# a=input("Eneter string: ")
# words = a.split(" ")
# for word in words:
#     i=len(word)-1
#     while i >= 0:
#         print(word[i], end=" ")
#         i-=1
#     print(end=" ")



##########count consonents ##############3333

word=input("Eneter string: ")
index=0
count=0
vowels="aeiou"

while index < len(word):
    print(index)
    count=0
    for char in word:
        if char not in ["a","e","i","o","u"]:
            count+=1
        
    print(count)
    break