class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = float("inf")

        while l <= r:
            # Handle case when current chunk is sorted, return early
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])
            
            # If left part is sorted then the minimum is on the right
            if nums[l] <= nums[mid]:
                l = mid + 1
            # If right part is sorted then the minimum is on the left
            else:
                r = mid - 1
        
        return res if res != float("inf") else -1