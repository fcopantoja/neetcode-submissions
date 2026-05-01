class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) # rows
        cols = len(text2) # cols
        matrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if text1[row] == text2[col]:
                    matrix[row][col] = 1 + matrix[row + 1][col + 1]
                else:
                    matrix[row][col] = max(matrix[row + 1][col], matrix[row][col + 1])

        
        return matrix[0][0]
        

    

        
        