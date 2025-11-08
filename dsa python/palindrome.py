
num=int(input("Enter number: "))
const=num
reversed_num=0
while num:
    digit=num%10                 
    reversed_num=reversed_num*10+digit
    num=num//10               


if reversed_num == const:
    print(f'{const} is palindrome')
else:
    print(f'{const} is not palindrome')