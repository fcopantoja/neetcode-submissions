class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for row in range(numRows):
            arr = []
            for i in range(row + 1):
                if i == 0 or i == row:
                    arr.append(1)
                else:
                    arr.append(result[row - 1][i - 1] + result[row - 1][i])
            result.append(arr)
        
        return result