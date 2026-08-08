from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        queue = deque(range(len(tickets)))

        time = 0

        while tickets[k] > 0:

            person = queue.popleft()

            tickets[person] -= 1
            time += 1

            if tickets[person] > 0:
                queue.append(person)

        return time