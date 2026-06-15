class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        n = len(nums)
        result_set = set()

        for num in nums:
            counter[num] += 1

            if counter[num] > n /3:
                result_set.add(num)
        
        return list(result_set)