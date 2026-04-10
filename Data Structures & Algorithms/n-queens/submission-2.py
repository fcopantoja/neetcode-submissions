class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        matrix = [["."] * n for _ in range(n)]
        result = []
        col_set = set()
        pos_diag = set()
        neg_diag = set()

        def backtracking(i):  # i -> row
            if i == n:
                copy = ["".join(row) for row in matrix]
                result.append(copy)
                return

            for j in range(n):  # j -> col
                if (
                    j in col_set or
                    (i + j) in pos_diag or
                    (i - j) in neg_diag
                ):
                    continue

                col_set.add(j)
                pos_diag.add(i + j)
                neg_diag.add(i - j)
                matrix[i][j] = "Q"

                backtracking(i + 1)

                col_set.remove(j)
                pos_diag.remove(i + j)
                neg_diag.remove(i - j)
                matrix[i][j] = "."

        backtracking(0)
        return result