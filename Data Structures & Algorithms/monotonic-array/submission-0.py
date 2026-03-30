class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_increasing = True
        is_decreasing = True
        n = len(nums)

        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                is_increasing = False

            if nums[i] > nums[i - 1]:
                is_decreasing = False

        return is_increasing or is_decreasing
                

        