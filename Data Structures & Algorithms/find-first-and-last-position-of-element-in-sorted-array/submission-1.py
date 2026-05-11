class Solution:
    def binary_search(self, nums, target, side="left"):
        l = 0
        r = len(nums) - 1
        res = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                res = mid
                if side == "left":
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return res


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums, target)
        right = self.binary_search(nums, target, side="right")
        return [left, right]
        