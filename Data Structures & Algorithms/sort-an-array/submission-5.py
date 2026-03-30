import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        
        pivot = random.choice(nums)
        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        res = self.sortArray(left) + mid + self.sortArray(right)
        return res
        

