class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = [-x for x in nums]
        heapq.heapify(hp)
        result = heapq.nsmallest(k, hp)
        return result[-1] * -1
