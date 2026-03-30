class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        mayority_num = n // 2
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
            if counter[num] > mayority_num:
                return num
        