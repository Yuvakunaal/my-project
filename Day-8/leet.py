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
# O(n) - time complexity
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

# O(1) - time complexity
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        
    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]

# https://leetcode.com/problems/remove-duplicate-letters/description/
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_occurrence = {char: i for i, char in enumerate(s)}
        print(last_occurrence)
        seen = set()
        for i, char in enumerate(s):
            if char not in seen:
                while (stack and char < stack[-1] and i < last_occurrence[stack[-1]]):
                    seen.remove(stack.pop())
                stack.append(char)
                seen.add(char)
            print(stack)
        return "".join(stack)

        
