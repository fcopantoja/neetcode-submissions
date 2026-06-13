class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        curr_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[curr_index] = nums[i]
                curr_index += 1
        
        for i in range(curr_index, len(nums)):
            nums[i] = 0
