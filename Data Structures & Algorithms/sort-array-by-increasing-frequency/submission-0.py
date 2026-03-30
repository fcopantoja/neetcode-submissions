class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        counts = sorted(counts.items(), key=lambda x: (x[1], -x[0]))
        result = []

        for num, freq in counts:
            result.extend([num] * freq)
    
        return result

        

        