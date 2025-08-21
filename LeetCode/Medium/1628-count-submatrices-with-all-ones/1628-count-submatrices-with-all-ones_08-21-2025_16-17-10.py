def check_rect_matrice(i: int, j: int, matrix: list[list[str]]):
    count = 0
    col = 0
    row = 0
    max_height = len(matrix)
    #expand downwards add 1 to count if valid
    #if reach the end of matrix or 0 then set as maxheight
    #got right one col then check from top again
    while j + col < len(matrix[0]):
        if (matrix[i][j + col] == 0):
            break
        row = 0
        while i + row < len(matrix) and row <= max_height:
            #check row till the end
            if (matrix[i+row][j+col] == 0):
                break
            row += 1
            count += 1
        max_height = row - 1
        col += 1
    
    return count
        
class Solution:
    def numSubmat(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        result = 0
        while i < m:
            j = 0
            while j < n:
                # print(i, j, matrix[i][j])
                if matrix[i][j] == 1:
                    count = check_rect_matrice(i, j, matrix)
                    matrix[i][j] += count - 1
                    result += count 
                j += 1
            i += 1

        return result