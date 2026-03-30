class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        def reverse_st(s, l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        reverse_st(nums, 0 , n - 1)
        reverse_st(nums, 0 , k - 1)
        reverse_st(nums, k , n - 1)
