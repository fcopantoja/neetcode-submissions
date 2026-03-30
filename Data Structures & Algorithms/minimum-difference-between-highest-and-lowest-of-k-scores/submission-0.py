class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = k - 1
        min_difference = float("inf")

        while r < len(nums):
            v = nums[r] - nums[l]
            min_difference = min(min_difference, v)
            r += 1
            l += 1
        
        return min_difference
            
        

