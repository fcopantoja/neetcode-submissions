class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        res = nums[0]

        for i in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            res = max(res, curr_sum)
        
        return res
        