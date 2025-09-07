def check_left(a_stack: list, stone: int) -> list:
    pop = a_stack.pop
    while a_stack and a_stack[-1] > 0: #if stack is nonempty and stone goes right
        difference = stone + a_stack[-1]
        if difference > 0: #if smaller than left
            return a_stack
        elif difference == 0: #if same size explode
            pop(-1)
            return a_stack
        elif difference < 0: #if bigger than left
            pop(-1)

    #if a_stack is empty then append
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