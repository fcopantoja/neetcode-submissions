class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        count = 0

        if window_sum // k >= threshold:
            count += 1

        for i in range(k, len(arr)):
            window_sum -= arr[i - k]
            window_sum += arr[i]

            if window_sum // k >= threshold:
                count += 1

        return count
                
            
