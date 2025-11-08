class Solution:
    def preToInfix(self, pre_exp):
        stack=[]
        for ch in pre_exp[::-1]:
            if ch.isalnum():
                stack.append(ch)
                
            else:
                last_oper=stack.pop()
                sec_last_oper=stack.pop()
                
                res=f"({last_oper}{ch}{sec_last_oper})"
                
                stack.append(res)
        return stack[-1]