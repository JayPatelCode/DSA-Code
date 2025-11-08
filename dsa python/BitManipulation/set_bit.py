

# 1101        13
# 0010         1 left shifted by 1 and now we perform or with num
# 1111        15

def bit_set(num:str,i)->bool:
    # bin=convert2bin(num)
    # print(bin)
    print(1<<i)
    return(num|(1<<i))
    
print(bit_set(13,1))