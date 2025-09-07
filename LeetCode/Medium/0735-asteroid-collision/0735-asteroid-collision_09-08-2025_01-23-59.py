def check_left(a_stack: list, stone: int) -> list:
    for i in reversed(a_stack):
        if i < 0:
            break
        if stone + i > 0:
            return a_stack
        elif stone + i == 0:
            a_stack.pop(-1)
            return a_stack
        elif stone + i < 0:
            a_stack.pop(-1)
    
    a_stack.append(stone)
    return a_stack


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        a_stack = []
        for i in asteroids:
            if i < 0:
                check_left(a_stack, i)
            else:
                a_stack.append(i)
        return a_stack