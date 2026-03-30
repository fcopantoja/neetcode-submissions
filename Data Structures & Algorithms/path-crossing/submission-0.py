class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {"N": [0, 1], "E": [1, 0], "S": [0, -1], "W": [-1, 0]}
        cur = (0,0)
        visited = set()
        visited.add(cur)

        for p in path:
            x, y = cur
            cur = (x + directions[p][0], y + directions[p][1])
            if cur in visited:
                return True
            visited.add(cur)

        return False

