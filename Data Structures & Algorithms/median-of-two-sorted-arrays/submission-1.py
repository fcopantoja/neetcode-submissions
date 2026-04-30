class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()

        if len(arr) % 2 == 0:
            mid = (len(arr) // 2 - 1)
            a = arr[mid]
            b = arr[mid + 1]
            return (a + b) / 2
        else:
            return arr[len(arr) // 2]
        