class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            num = nums[middle]
            if num == target:
                return middle

            # left portion
            if nums[middle] >= nums[left]:
                if target < nums[left]:
                    left = middle + 1
                elif target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if target < nums[middle]:
                    right = middle - 1
                elif target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1

        return -1