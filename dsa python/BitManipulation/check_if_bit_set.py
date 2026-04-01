1101


# def check_bit_set(bin:str,i)->bool:
#     if (bin & (1<<i)) != 0:
#         return True
#     else:
#         return False


# print(check_bit_set(13,3))



# def check_bit_set_right_shift(bin:str,i)->bool:
#     if (1 & (bin>> i)) ==1:
#         return True
#     else:
#         return False


# print(check_bit_set_right_shift(13,3))






1100

def check_bit_set(num:str,i)->bool:
    return True if (num & 1<<i) else False

print(check_bit_set(12,3))