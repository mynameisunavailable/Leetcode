import numpy as np

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        # insert zeroes at first row and first col
        first_row = [0 for x in matrix[0]]
        matrix.insert(0, first_row)
        for i in matrix:
            i.insert(0, 0)
        
        i = 1
        while i < m + 1:
            j = 1
            while j < n + 1:
                # print(i, j, matrix[i][j])
                if matrix[i][j] == 1:
                    min_num = min(matrix[i - 1][j - 1],
                    matrix[i][j - 1],
                    matrix[i - 1][j]
                    )
                    matrix[i][j] += min_num
                j += 1
            i += 1

        result = 0
        for i in matrix:
            result += sum(i)
        return result