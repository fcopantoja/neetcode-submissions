class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set()
        res = 0

        for num in nums:
            sett.add(num)

        for num in nums:
            # first in sequence
            if num in sett and (num - 1) not in sett:
                cur = num
                cnt = 0

                while cur in sett:
                    sett.remove(cur)
                    cur += 1
                    cnt += 1
                
                res = max(res, cnt)
        
        return res