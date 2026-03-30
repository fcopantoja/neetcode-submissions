class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        sett = set(nums)
        res = []

        for i in range(1, len(nums) + 1):
            if i not in sett:
                res.append(i)
        
        return res
