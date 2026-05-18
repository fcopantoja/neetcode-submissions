class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def can_split(mid):
            k_needed = 1
            curr_sum = 0
            

            for n in nums:
                if (curr_sum + n) > mid:
                    curr_sum = 0
                    k_needed += 1
                curr_sum += n

            return k_needed <= k
        

        l = max(nums)
        r = sum(nums)
        res = r

        while l <= r:
            mid = (l + r) // 2

            if can_split(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res