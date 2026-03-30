class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n * (n + 1) // 2
        nums_sum = sum(nums)
        print(result, nums_sum)
        if nums_sum == result:
            return 0
        else:
            return result - nums_sum