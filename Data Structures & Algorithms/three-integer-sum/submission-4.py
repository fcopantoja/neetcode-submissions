class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index, num in enumerate(nums):
            left = index + 1
            right = len(nums) - 1

            if index > 0 and num == nums[index - 1]:
                continue
            
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum == 0:
                    result.append([nums[index], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
        return result