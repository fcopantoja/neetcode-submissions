class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        max_product = nums[0]
        min_product = nums[0]

        for num in nums[1:]:
            tmp_max = max(num, num * max_product, num * min_product)
            min_product = min(num, num * max_product, num * min_product)
            max_product = tmp_max
            res = max(res, max_product)
        
        return res