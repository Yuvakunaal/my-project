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
