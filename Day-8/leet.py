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
s = Solution()
print(s.simplifyPath("/home/user/Documents/../Pictures"))

        
