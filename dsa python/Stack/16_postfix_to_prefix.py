class Solution:
    def postToPre(self, post_exp):
        stack=[]
        for ch in post_exp:
            if ch.isalnum():
                stack.append(ch)
                
            else:
                last_oper=stack.pop()
                sec_last_oper=stack.pop()
                
                res=f"{ch}{sec_last_oper}{last_oper}"
                
                stack.append(res)
        return stack[-1]