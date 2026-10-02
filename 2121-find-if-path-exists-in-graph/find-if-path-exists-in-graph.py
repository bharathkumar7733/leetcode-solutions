from collections import deque

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = {}

        for i in range(n):
            graph[i] = []

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([source])
        visited = {source}

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        return False