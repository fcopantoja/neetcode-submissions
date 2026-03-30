class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n * (n + 1) // 2
        nums_sum = sum(nums)
        return 0 if nums_sum == result else result - nums_sum
