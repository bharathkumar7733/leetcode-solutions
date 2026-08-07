

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            alive = True
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(asteroid) < stack[-1]:
                    alive = False
                    break
                elif abs(asteroid) > stack[-1]:
                    stack.pop()
                else:
                    stack.pop()
                    alive = False
                    break
            if alive:
                stack.append(asteroid)

        return stack
