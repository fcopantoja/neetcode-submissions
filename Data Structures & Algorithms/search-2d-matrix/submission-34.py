class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)


        while top <= bottom:
            row = (top + bottom) // 2
            if row > (len(matrix) - 1):
                return False

            if matrix[row][0] <= target <= matrix[row][-1]:
                break
            
            if target < matrix[row][0]:
                bottom = row - 1
            else:
                top = row + 1
        
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True

            if matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
        



            

        