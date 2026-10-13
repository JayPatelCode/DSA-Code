class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        total = 0

        if x >= y:
            first, second = 'a', 'b'
            points = x
        else:
            first, second = 'b', 'a'
            points = y

        for ch in s:
            if stack and stack[-1] == first and ch == second:
                stack.pop()
                total += points
            else:
                stack.append(ch)

        remaining = ''.join(stack)
        stack = []

        for ch in remaining:
            if stack and stack[-1] == second and ch == first:
                stack.pop()
                total += min(x, y)
            else:
                stack.append(ch)

        return total