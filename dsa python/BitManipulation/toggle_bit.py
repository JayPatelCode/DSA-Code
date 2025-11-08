
# 1101        13
# 0010
# 1111

def toggle_bit(num:str,i)->bool:
    # bin=convert2bin(num)
    # print(bin)
    
    return(num ^((1<<i)))
    
print(toggle_bit(13,1))