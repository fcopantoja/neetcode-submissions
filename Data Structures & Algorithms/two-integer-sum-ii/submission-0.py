class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, number in enumerate(numbers):
            desired = target - number
            index_found = self.binary_search(numbers, desired)
            if index_found:
                return [index + 1, index_found + 1]

        return []

    def binary_search(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            middle = (left + right) // 2
            if arr[middle] == target:
                return middle
            if arr[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return None    