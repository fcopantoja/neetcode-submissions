class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # i's corresponds to text2
        # j's corresponds to text1
        matrix = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        for i in range(len(text2) - 1, -1, -1):
            for j in range(len(text1) - 1, -1, -1):
                if text2[i] == text1[j]:
                    matrix[i][j] = 1 + matrix[i + 1][j + 1]
                else:
                    matrix[i][j] = max(matrix[i + 1][j], matrix[i][j + 1])
        
        return matrix[0][0]

    

        
        