class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        prefix_sum = [0] * n
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        
        posfix_sum = [0] * n
        for i in range(n - 2, -1, -1):
            posfix_sum[i] = nums[i + 1] + posfix_sum[i + 1]

        for i in range(n):
            if prefix_sum[i] == posfix_sum[i]:
                return i
        
        return -1