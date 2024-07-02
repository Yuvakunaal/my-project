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

# https://leetcode.com/problems/132-pattern/description/
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        a = -float('inf') #initializing with -infinity
        s = []
        print(nums[::-1])
        for i in nums[::-1]:
            print(a)
            if(i < a):
                return True
            while(s and s[-1] < i):
                a = s.pop()
            s.append(i)
        return False

# https://leetcode.com/problems/valid-parenthesis-string/description/
class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1

            elif char == ')':
                if min_open > 0:
                    min_open -= 1
                max_open -= 1

            elif char == '*':
                if min_open > 0:
                    min_open -= 1
                max_open += 1

            if max_open < 0:
                return False
                
        return min_open == 0




        
