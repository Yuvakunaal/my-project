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

# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c=0
        for i,j in zip(s1,s2): # -> merged strs will be in tuple form
            if i!=j:
                c+=1
        return s1==s2 or sorted(s1)==sorted(s2) and c==2

# https://leetcode.com/problems/make-three-strings-equal/description/
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        pref_len = 0
        for a, b, c in zip(s1, s2, s3):
            if a == b == c:
                pref_len += 1
            else:
                break
        if not pref_len:
            return -1
        return sum(len(s) - pref_len for s in (s1, s2, s3))

# https://leetcode.com/problems/reorganize-string/description/
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        max_heap = [(-count,char) for char,count in freq.items()]
        heapq.heapify(max_heap)
        prev_char = ''
        prev_count = 0
        result = []

        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            if prev_count < 0:
                heapq.heappush(max_heap,(prev_count,prev_char))
            prev_char = char
            prev_count = count+1
            
        if len(result) != len(s):
            return ""
        return "".join(result)

# https://leetcode.com/problems/magical-string/description/
class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0 
        s = [1,2,2]
        i = 2
        while len(s) < n: 
            s.extend(s[i] * [3 ^ s[-1]]) # ^ = XOR (one is true and other is false)
            i += 1
        return s[:n].count(1)

# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        p1 = sorted(p)
        for i in range(len(s)-len(p)+1):
            a = s[i:i+len(p)]
            if sorted(a) == p1:
                ans.append(i)
        return ans

