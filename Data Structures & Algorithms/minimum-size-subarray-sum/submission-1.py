class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        left, right = 0, 0
        curr_sum = 0

        while right < len(nums):
            curr_sum += nums[right]

            # handle curent sum equals or greater than target
            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            
            right += 1

        return min_length if min_length != float("inf") else 0
