import collections
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counter = collections.Counter(tuple(x) for x in grid)
        col_counter = collections.Counter(tuple(x) for x in zip(*grid))
        total = [row_counter[x] * col_counter[x] for x in row_counter]
        return sum(total)
