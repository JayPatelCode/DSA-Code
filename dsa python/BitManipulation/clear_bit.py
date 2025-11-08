# 1<<2                    # 1<<i
# 0001<<2
# ~(0100)              #Not operator as we only need to clear that bit to 0
# 1011

# 1101        13
# 1011          and operation
# 1001        9
def clear_bit(num:str,i)->bool:
    # bin=convert2bin(num)
    # print(bin)
    
    return(num &(~(1<<i)))
    
print(clear_bit(13,2))