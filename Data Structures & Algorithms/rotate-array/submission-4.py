class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        k = k % len(nums)

        def reverse_st(s, l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        
        reverse_st(nums, 0 , len(nums) - 1)
        reverse_st(nums, 0 , k - 1)
        reverse_st(nums, k , len(nums) - 1)
