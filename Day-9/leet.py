# https://leetcode.com/problems/running-sum-of-1d-array/description/
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums

# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a = sum(nums)
        b = sum([int(digit) for num in nums for digit in str(num)])
        return abs(a-b)

# https://leetcode.com/problems/find-the-highest-altitude/description/
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0,0)
        for i in range(1,len(gain)):
            gain[i]+=gain[i-1]
        return max(gain)

# https://leetcode.com/problems/find-the-highest-altitude/description/
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        return sum([sum(arr[i:j+1]) for i in range(len(arr)) for j in range(i, len(arr)) if (j - i + 1) % 2 != 0])

# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (sorted(nums)[-2]-1)*(sorted(nums)[-1]-1)

# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num = set(nums)
        return [i for i in range(1,len(nums)+1) if i not in num]

# https://leetcode.com/problems/count-number-of-nice-subarrays/description/
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = {0: 1}
        count_odds = 0
        result = 0

        for num in nums:
            if num % 2 == 1:
                count_odds += 1
            #if there are subarrays ending at the current index with exactly k odd numbers
            if count_odds - k in counts: 
                result += counts[count_odds - k]
            if count_odds in counts:
                counts[count_odds] += 1
            else:
                counts[count_odds] = 1
        
        return result
    
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        target = k * threshold 

        curr = 0
        for i in range(k - 1):
            curr += arr[i]
        for i in range(k - 1, len(arr)):
            curr += arr[i]
            if curr >= target:
                count += 1
            curr -= arr[i - k + 1]
        
        return count

# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        count_ones = 0
        left = 0
        
        for right in range(n):
            if nums[right] == 1:
                count_ones += 1
            while right - left + 1 - count_ones > 1:
                if nums[left] == 1:
                    count_ones -= 1
                left += 1
            max_len = max(max_len, right - left)
        
        return max_len