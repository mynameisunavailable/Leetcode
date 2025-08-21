def check_line_valid(i: int, j: int, matrix: list[list[str]], max_square_side: int):
    count = 0
    while (count < max_square_side):
        if (j + count + 1 > len(matrix[0])):
            return False
        if matrix[i][j + count] != 1:
            return False
        count += 1
    return True

def check_sq_valid(i: int, j: int, matrix: list[list[str]], max_square_side: int):
    count = 0
    while count < max_square_side:
        if (i + count + 1 > len(matrix)):
            return False
        if check_line_valid(i + count, j, matrix, max_square_side) == False:
            return False
        count += 1
    return True

def check_max_sq_side(i: int, j: int, matrix: list[list[str]], max_square_side: int) -> int:
    if len(matrix) == 1 or len(matrix[0]) == 1:
        return 1
    while True:
        if (check_sq_valid(i, j, matrix, max_square_side) == False):
            return (max_square_side - 1)
        max_square_side += 1

    
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        while i < m:
            j = 0
            while j < n:
                # print(matrix[i][j])
                if matrix[i][j] == 1:
                    max_squares = check_max_sq_side(i, j, matrix, 2)
                    matrix[i][j] = max_squares
                j += 1
            i += 1

        result = 0
        for i in matrix:
            result += sum(i)
        return result