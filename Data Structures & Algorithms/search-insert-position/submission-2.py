class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = 0

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                r -= 1
            else:
                l += 1
        
        if mid == len(nums) - 1:
            if target > nums[mid]:
                mid += 1
            #else:
            #    mid -= 1
        
        return mid
