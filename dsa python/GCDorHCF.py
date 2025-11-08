#8 / 14   divisor/divident
# then we divide 14 by 8 if it is 0 then divisor is 



a=int(input("Enter number a: "))
b=int(input("Enter number b: "))

divisor=min(a,b)
dividend=max(a,b)

while dividend%divisor !=0:
    temp=dividend
    dividend=divisor
    divisor=temp%divisor
    
print(divisor)
    
    