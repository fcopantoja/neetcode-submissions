class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [[1]]

        for i in range(1, rowIndex + 1):
            row = [1] * (i + 1)
            for j in range(i + 1):
                if j == 0 or j == i:
                    continue
                row[j] = rows[i-1][j-1] + rows[i-1][j]
            rows.append(row)
            
        return rows[rowIndex]