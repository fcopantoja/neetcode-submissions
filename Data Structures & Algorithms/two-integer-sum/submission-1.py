class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for index, num in enumerate(nums):
            desired = target - num
            if desired in hmap:
                return [hmap[desired], index]
            hmap[num] = index
        