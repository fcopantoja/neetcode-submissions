class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        rows = len(image)
        cols = len(image[0])
        queue = deque([(sr, sc)])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        start_color = image[sr][sc]
        
        while queue:
            node = queue.popleft()
            visited.add(node)
            image[node[0]][node[1]] = color

            for direction in directions:
                dr = node[0] + direction[0]
                dc = node[1] + direction[1]

                if (
                    dr in range(rows) and
                    dc in range(cols) and
                    (dr, dc) not in visited and
                    image[dr][dc] == start_color
                ):
                    visited.add((dr, dc))
                    queue.append((dr, dc))

        return image



