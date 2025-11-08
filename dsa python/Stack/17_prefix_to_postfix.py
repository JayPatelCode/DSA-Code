class Solution:
    def preToPost(self, pre_exp):
        stack=[]
        for ch in pre_exp[::-1]:
            if ch.isalnum():
                stack.append(ch)
                
            else:
                sec_last_oper =stack.pop()
                last_oper=stack.pop()
                
                res=f"{sec_last_oper}{last_oper}{ch}"
                
                stack.append(res)
        return stack[-1]