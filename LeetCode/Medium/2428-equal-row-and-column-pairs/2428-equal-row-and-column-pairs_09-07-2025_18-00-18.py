def rotate_grid_90(grid: list[list[int]]):
    row_len = len(grid)
    col_len = len(grid[0])
    rotated_grid = []
    temp_row = []
    for i in range(row_len):
        for j in range(col_len):
            temp_row.append(grid[j][i])
        rotated_grid.append(temp_row)
        temp_row = []

    return rotated_grid

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rotated_grid = rotate_grid_90(grid)
        grid_dict = {}
        #find out how many occurance of row items
        for i in grid:
            i = tuple(i)
            grid_dict[i] = grid_dict.get(i, 0) + 1
        #each occurance of row + 1 if found col item
        total = 0
        for i in rotated_grid:
            i = tuple(i)
            if grid_dict.get(i, 0) > 0:
                total += grid_dict[i]

        return total