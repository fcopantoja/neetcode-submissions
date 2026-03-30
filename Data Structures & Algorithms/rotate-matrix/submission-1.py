class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1
        top = 0
        bottom = right

        while left < right:
            top, bottom = left, right
            for i in range(right - left):
                top_left = matrix[top][left + i]

                # move bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move bottom right to top bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move top_left to top right
                matrix[top + i][right] = top_left

            left += 1
            right -= 1

