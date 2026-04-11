class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        index = 0
        for i in range(3):
            while counts[i] > 0:
                nums[index] = i
                index += 1
                counts[i] -= 1


        """l = 0
        r = len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]        
                l += 1
            elif nums[i] == 2 and i < r:
                nums[i], nums[r] = nums[r], nums[i]        
                r -= 1
                i -= 1
            
            i += 1"""
        