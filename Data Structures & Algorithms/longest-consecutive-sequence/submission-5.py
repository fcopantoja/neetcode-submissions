class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        res = 0

        for num in nums:
            if (num - 1) not in sett:
                longest = 1
                while (num + 1) in sett:
                    longest += 1
                    num += 1
                
                res = max(res, longest)
        
        return res
   