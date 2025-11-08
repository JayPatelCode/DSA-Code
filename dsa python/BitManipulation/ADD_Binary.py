a = "11"
b = "1"
a,b=int(a,2), int(b,2)

while b:
    without_carry=a ^ b #######exor
    carry = (a & b)<<1 ########bitwise and operation and then left shift by one
    a,b=without_carry,carry
print(bin(a)[2:])