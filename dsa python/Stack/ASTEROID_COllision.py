class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n=len(asteroids)
        stack=[]
        for a in asteroids:
            if a>0:
                stack.append(a)
            else:
                while len(stack)!=0 and stack[-1]>0 and abs(a)>stack[-1]:
                    stack.pop()

                if len(stack)!=0 and stack[-1]==abs(a):
                    stack.pop()
                
                elif len(stack)==0 or stack[-1]<0:
                    stack.append(a)
        return stack