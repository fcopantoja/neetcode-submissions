class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums2)
        hmap = {}
        stack = []

        for idx, num in enumerate(nums2):
            while stack and stack[-1][0] < num:
                n, j = stack.pop()
                hmap[n] = num

            stack.append((num, idx))
            print(stack)
        
        print(hmap)
        result = []
        for num in nums1:
            result.append(hmap.get(num, -1))
        return result

            


            



