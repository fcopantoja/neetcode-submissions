class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0

        for num in nums:
            seq = 0
            if (num - 1) not in sett:
                while num in sett:
                    seq += 1
                    num += 1
                longest = max(longest, seq)

        return longest