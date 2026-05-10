class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        left_a = 0
        left_b = 0

        while left_a < len(nums1) and left_b < len(nums2):
            if nums1[left_a] < nums2[left_b]:
                arr.append(nums1[left_a])
                left_a += 1
            else:
                arr.append(nums2[left_b])
                left_b += 1
        print(left_a, left_b)
        if left_b < len(nums2):
            arr += nums2[left_b:]
        elif left_a < len(nums1):
            arr += nums1[left_a:]
        
        print(arr)
        length = len(arr)
        if length % 2 == 0:            
            return (arr[length // 2 - 1] + arr[length // 2]) / 2
        else:
            return arr[length // 2]

        