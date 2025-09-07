class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rotated_grid = zip(*grid)
        grid_dict = {}
        #find out how many occurance of row items
        for i in grid:
            i = tuple(i)
            grid_dict[i] = grid_dict.get(i, 0) + 1
        #each occurance of row + 1 if found col item
        total = 0
        for i in rotated_grid:
            i = tuple(i)
            total += grid_dict.get(i, 0)

        return total
