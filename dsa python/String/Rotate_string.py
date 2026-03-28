s="abcde"
goal="cdeab"
n=len(s)
curr_s=s
for i in range(n):
    if curr_s==goal:
        print(True)
        break
    curr_s=curr_s[-1]+curr_s[:-1]
print(False)