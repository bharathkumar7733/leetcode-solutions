from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        queue = deque([0])
        visited = {0}

        while queue:
            node = queue.popleft()

            for nei in rooms[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        return len(visited) == len(rooms)