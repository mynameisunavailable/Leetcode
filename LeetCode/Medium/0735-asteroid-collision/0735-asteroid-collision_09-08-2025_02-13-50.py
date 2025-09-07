class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        a_stack = []
        append, pop = a_stack.append, a_stack.pop
        for i in asteroids:
            if i < 0:
                while a_stack and a_stack[-1] > 0: #if stack is nonempty and stone goes right
                    difference = i + a_stack[-1]
                    if difference > 0: #if smaller than left
                        break
                    elif difference == 0: #if same size explode
                        pop(-1)
                        break
                    elif difference < 0: #if bigger than left
                        pop(-1)
                else:
                    append(i)
            else:
                append(i)
        return a_stack