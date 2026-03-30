class Solution:
    def findDisappearedNumbersWithExtraSpace(self, nums: List[int]) -> List[int]:
        sett = set(nums)
        res = []

        for i in range(1, len(nums) + 1):
            if i not in sett:
                res.append(i)
        
        return res


    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res
