class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        result = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            else:
                result = max(result, ones)
                ones = 0
        
        return max(result, ones)


