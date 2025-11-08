# 011          3
# 100        4

# 111  exor

# 001    left shift by i
# 001       and with ans



# def convert_a_to_b(a,b)->int:
#     ans=a^b
#     count=0
#     for i in range(32): 
#         if (ans & (1<< i)) !=0:
#             count+=1
#     return count

# print(convert_a_to_b(3,4))





# 011
# 100
# 111

# 1010
# 0111
# 1101

# Now we count how many 1s are in 1101:
# Loop 1:

# ans = 1101 (binary)
# Last bit: 1101 & 1 = 1 ✓ (it's a 1, so count++)
# count = 1
# Shift right: 1101 >> 1 = 110

# Loop 2:

# ans = 110 (binary)
# Last bit: 110 & 1 = 0 (it's a 0, so skip)
# count = 1
# Shift right: 110 >> 1 = 11

# Loop 3:

# ans = 11 (binary)
# Last bit: 11 & 1 = 1 ✓ (it's a 1, so count++)
# count = 2
# Shift right: 11 >> 1 = 1

# Loop 4:

# ans = 1 (binary)
# Last bit: 1 & 1 = 1 ✓ (it's a 1, so count++)
# count = 3
# Shift right: 1 >> 1 = 0

# Loop ends (ans = 0)

def convert_a_to_b(a,b)->int:
    ans=a^b
    count=0
    # print(ans)
    while ans:
        if ans& 1:
            count+=1
        ans=ans>>1
    return count
print(convert_a_to_b(10,7))