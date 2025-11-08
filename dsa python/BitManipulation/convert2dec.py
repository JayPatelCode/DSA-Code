def convert2dec(bin:str)->int: #1100
    dec_num=0
    power=0
    index=len(bin)-1
    print(index, "index")
    while index>=0:
        print(int(bin[index]))
        num= (int(bin[index]) * (2**power))
        dec_num+=num
        print(num, "num")
        print(dec_num, "dec")
        power+=1
        index-=1
    return dec_num

print(convert2dec("1100"))