# s="cadbzabcd"
# n=len(s)

# maxi=0
# for i in range(n):
#     st=set()
#     for j in range(i,n):
#         if s[j] in st:
#             break
#         maxi=max(maxi,j-i+1)
#         st.add(s[j])
        
# print(maxi)
        


#optimal
s="cadbzabcd"
n=len(s)
my_dict={}
left=0
right=0

maxi=0

while right<n:
    if s[right] in my_dict:
        left=max(left, my_dict[s[right]]+1)
    
    maxi=max(maxi,right-left+1)
    my_dict[s[right]]=right
    right+=1
print(maxi)