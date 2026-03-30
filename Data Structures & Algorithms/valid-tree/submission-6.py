from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen = set()
        queue = deque([(0, -1)])  # (node, parent)

        while queue:
            node, parent = queue.popleft()

            if node in seen:
                return False

            seen.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                seen.add(node)
                queue.append((nei, node))

        return len(seen) == n