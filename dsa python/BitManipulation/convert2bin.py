def convert2bin(num):
    res=""

    while num>0:
        if num%2==1:
            res+="1"
        else:
            res+="0"

        num=num//2
    res=res[::-1]
    return res

# print(convert2bin(8))

# O(log2n) both time and space
