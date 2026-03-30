class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_number = float("inf")

        while left <= right:
            if nums[left] < nums[right]:
                min_number = min(min_number, nums[left])
                break


            middle = (left + right) // 2
            num = nums[middle]
            min_number = min(num, min_number)

            if num >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        
        return min_number

        