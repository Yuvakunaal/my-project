# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/description/
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        current_string = ""
        for word in words:
            current_string += word
            if current_string == s:
                return True
            elif len(current_string) > len(s):
                return False
        return False