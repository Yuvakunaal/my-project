# https://leetcode.com/problems/simplify-path/description/
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')
        for part in parts:
            if part == '..':
                if stack:
                    stack.pop()
            elif part and part != '.':
                stack.append(part)
        simplified_path = '/' + '/'.join(stack)
        return simplified_path

# https://leetcode.com/problems/min-stack/description/
class MinStack:
    def __init__(self):
        self.stack = []
        return None
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        return None

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        self.stack.pop()
        return None

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return min(self.stack)


        
