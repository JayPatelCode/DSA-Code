class Solution:
    def postToInfix(self, postfix):      # 1 here first we will check that is is between a-z or A-Z or 1 to 9 then directly append to slack
        stack=[]                         # 2 if it is operand then pop last 2 element from stack and add operator in between and around put ()
        for char in postfix:             # 3 at last return the last only present expression from stack
            if char.isalnum():
                stack.append(char)
              
            else:  
                last_ele=stack.pop()
                sec_last=stack.pop()
                
                new_expr=f"({sec_last}{char}{last_ele})"
                
                stack.append(new_expr)
                
                
        return stack[-1]