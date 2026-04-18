class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                    r < 0 or r >= rows or
                    c < 0 or c >= cols or
                    (r, c) in visited or
                    board[r][c] != word[i]
            ):
                return False

            visited.add((r, c))
            res1 = dfs(r + 1, c, i + 1)
            res2 = dfs(r - 1, c, i + 1)
            res3 = dfs(r, c + 1, i + 1)
            res4 = dfs(r, c - 1, i + 1)
            visited.remove((r, c))
            return any([res1, res2, res3, res4])

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True

        return False