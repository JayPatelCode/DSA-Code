def square_no(no):
    total=0
    while no>0:
        last_dig=no%10
        total=total+(last_dig*last_dig)
        no=no//10
    return total
print(square_no(94))





def happy(n):
    visited=set()
    while square_no(n) not in visited:
        total_sum=square_no(n)
        if total_sum==1:
            return True
        else:
            visited.add(total_sum)
            n=total_sum
    return False

if happy(94)==True:
    print("No is happy number")

else:
    print("No is not an happy number")