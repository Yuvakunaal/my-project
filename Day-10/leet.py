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

# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_len = lambda a, b: a if b == 0 else gcd_len(b, a % b)
        return str1[:gcd_len(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ""