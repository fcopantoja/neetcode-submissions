class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            print(nums[i], nums[i - 1])
            if nums[i] % 2 == nums[i - 1] % 2:
                return False
            
        return True