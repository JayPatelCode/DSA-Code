# 10      2
# 110     4
# 1000    8
# 10000   16
def p_of_2(num:str)->bool:              ###############removing right most bit
    return(num & (num-1)==0)
    
print(p_of_2(16))