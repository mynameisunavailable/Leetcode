import collections
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counter = collections.Counter(tuple(x) for x in grid)
        return sum(row_counter[tuple(x)] for x in zip(*grid))