class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)

        for num in nums1:
            counter1[num] += 1

        for num in nums2:
            counter2[num] += 1
        
        intersection = set(counter1.keys()) & set(counter2.keys())
        return list(intersection)