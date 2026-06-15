class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        mayority_num = n // 2
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
            if counter[num] > mayority_num:
                return num
        
    
    def majorityElement(self, nums: List[int]) -> int:
        curr_num = nums[0]
        curr_count = 1

        for i in range(1, len(nums)):
            n = nums[i]
            if n == curr_num:
                curr_count += 1
            elif n != curr_num:
                if curr_count == 1:
                    curr_num = n
                    curr_count = 1
                else:
                    curr_count -= 1
        
        return curr_num
        

