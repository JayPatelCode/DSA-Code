class Solution:
    
    def precedence(self,ch):                         # 1) reverse the string
        if ch=="+" or ch=="-":                       # 2)  Swap parentheses: ( becomes ) and ) becomes (
            return 1                                 # 3) infix to postfix
        elif ch=="*" or ch=="/":                     # 4) return reversed result string
            return 2
        elif ch=="^":
            return 3
        return 0
    def infixToPrefix(self, s):
        rev_str=s[::-1]
        result=[]
        stack=[]
        for ch in rev_str:
            if "a"<=ch<="z" or "A"<=ch<="Z" or "0"<=ch<="9":
                result.append(ch)
            elif ch==")":
                stack.append(ch)
                
            elif ch=="(":
                while stack and stack[-1]!=")":
                    result.append(stack.pop())
                stack.pop()
        
            else:
                if ch=="^":
                    while stack and stack[-1] != ")" and self.precedence(stack[-1]) >= self.precedence(ch):
                        result.append(stack.pop())
                else:
                    while stack and stack[-1] != ")" and self.precedence(stack[-1]) > self.precedence(ch):
                        result.append(stack.pop())
                stack.append(ch)
            
          
        while stack:
            result.append(stack.pop())
            
        ans=result[::-1]
        return "".join(ans)