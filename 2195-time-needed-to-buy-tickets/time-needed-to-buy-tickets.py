from collections import deque
from typing import List  

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([(t, i) for i, t in enumerate(tickets)])  
        operations = 0

        while queue:
            ele, idx = queue.popleft()   
            ele -= 1
            operations += 1

            if ele > 0:
                queue.append((ele, idx)) 

            if idx == k and ele == 0:   
                return operations
