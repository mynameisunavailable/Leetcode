class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        a_stack = []
        for i in asteroids:
            if i < 0 and a_stack:
                while True:
                    if a_stack and a_stack[-1] > 0:
                        if a_stack[-1] + i < 0:
                            a_stack.pop(-1)
                        else:
                            break
                    else:
                        a_stack.append(i)
                        break
                if a_stack[-1] + i == 0:
                    a_stack.pop(-1)
            else:
                a_stack.append(i)
        return a_stack