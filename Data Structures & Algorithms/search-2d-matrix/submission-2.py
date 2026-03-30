class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom = 0
        top = len(matrix) - 1
        middle = (bottom + top) // 2

        while bottom <= top:
            middle = (bottom + top) // 2
            if matrix[middle][0] == target or matrix[middle][-1] == target:
                return True
            if matrix[middle][0] < target and matrix[middle][-1] > target:
                break
            if matrix[middle][0] < target:
                bottom = middle + 1
            else:
                top = middle - 1

        return self.binary_search(matrix[middle], target)
    
    def binary_search(self, arr: List[int], target: int):
        left = 0
        right = len(arr) - 1

        while left <= right:
            middle = (left + right) // 2
            if arr[middle] == target:
                return True

            if arr[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return False