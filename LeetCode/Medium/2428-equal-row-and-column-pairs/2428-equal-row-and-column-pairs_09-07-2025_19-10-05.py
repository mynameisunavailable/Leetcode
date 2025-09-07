import collections
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counter = collections.Counter(tuple(x) for x in grid)
        total_list = [row_counter[tuple(x)] for x in zip(*grid)]
        total = sum(total_list)
        return total
