class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        idx = 0
        for i in range(counter[0]):
            nums[idx] = 0
            idx += 1

        for i in range(counter[1]):
            nums[idx] = 1
            idx += 1

        for i in range(counter[2]):
            nums[idx] = 2
            idx += 1
        
        