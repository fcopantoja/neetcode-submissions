class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        n = len(arr)
        print(arr, arr[n // 2])

        if len(arr) % 2 == 1:
            return arr[n // 2]
        
        middle = (n // 2) - 1
        return (arr[middle] + arr[middle + 1]) / 2