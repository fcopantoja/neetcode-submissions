class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        current_sum = nums[0]
        res = current_sum

        for r in range(1, n):
            if nums[r] > nums[r - 1]:
                current_sum += nums[r]
                res = max(res, current_sum)
            else:
                current_sum = nums[r]
                l = r

        return res