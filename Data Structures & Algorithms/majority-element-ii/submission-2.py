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

    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

            if len(counter) <= 2:
                continue
            
            new_counter = defaultdict(int)
            for k, v in counter.items():
                if v > 1:
                    new_counter[k] = v - 1
            
            counter = new_counter

        res = []
        for num in counter:
            if nums.count(num) > len(nums) // 3:
                res.append(num)

        return res
        
        