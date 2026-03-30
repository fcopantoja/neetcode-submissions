class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        postfix_sum = [-1] * len(arr)
        maximum = -1

        for i in range(len(arr) - 2, -1, -1):
            postfix_sum[i] = max(arr[i + 1], postfix_sum[i + 1])
        
        return postfix_sum