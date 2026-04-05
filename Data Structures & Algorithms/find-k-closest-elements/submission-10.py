import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        new_arr = sorted(arr, key=lambda n: (abs(n - x), n))
        return sorted(new_arr[:k])
        
            