class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)

        for idx, num in enumerate(nums1):
            left = nums2.index(num)
            right = left

            while right < len(nums2):
                if num < nums2[right]:
                    result[idx] = nums2[right]
                    break
                right += 1
        
        return result
            


            



