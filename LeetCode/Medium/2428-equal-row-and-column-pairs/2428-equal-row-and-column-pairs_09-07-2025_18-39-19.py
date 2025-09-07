import collections
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        #find out how many occurance of row items
        row_counter = collections.Counter()
        for i in grid:
            i = tuple(i)
            row_counter[i] += 1
        #each occurance of row + 1 if found col item
        col_counter = collections.Counter()
        for i in zip(*grid):
            i = tuple(i)
            col_counter[i] += 1
        total = 0
        for i in row_counter:
            total += row_counter[i] * col_counter[i]

        return total
