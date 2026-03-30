class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            v1 = dp[i - 1]
            v2 = nums[i] + dp[i - 2]
            dp[i] = max(v1, v2)
            
        return dp[-1]