nums=[3,30,34,5,9]
nums=list(map(str,nums))
nums.sort(key=lambda x:x*10,reverse=True)
result="".join(nums)
print("0" if result[0] =='0' else result)
