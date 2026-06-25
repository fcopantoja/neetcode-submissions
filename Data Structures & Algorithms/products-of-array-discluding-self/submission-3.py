class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        posfix = [1] * len(nums)
        result = []    
        n = len(nums)

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            posfix[i] = posfix[i + 1] * nums[i + 1]
        
        for i in range(n):
            result.append(prefix[i] * posfix[i])
        
        return result

        
        