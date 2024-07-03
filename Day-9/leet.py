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

