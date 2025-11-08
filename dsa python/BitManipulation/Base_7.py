num = 100
# Output: "202"
if num==0:
    print("0")

reminders=[]
original_num=num
num=abs(num)
while num>0:
    rem=num%7
    reminders.append(str(rem))
    num=num//7
if original_num<0:
    reminders.append("-")
reminders.reverse()
print("".join(reminders))