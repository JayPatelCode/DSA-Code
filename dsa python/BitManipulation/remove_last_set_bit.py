
# 1101
def remove_last_set_bit(num:str)->bool:              ###############removing right most bit
    return(num & (num-1))
    
print(remove_last_set_bit(13))