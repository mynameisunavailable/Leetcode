#checks lowest value from matrix[i - 1][j - 1] and matrix[i][j - 1] and matrix[i - 1][j]
def check_lowest_val(i: int, j: int, matrix: list[list[int]]):
    return min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j])

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #convert all string value into numbers
        new_matrix = [[1 if (x == "1") else 0 for x in row] for row in matrix]
        #fill a top row and left most col with 0 for boundary
        top_row = [0 for x in new_matrix[0]]
        new_matrix.insert(0, top_row)
        for i in new_matrix:
            i.insert(0, 0)
        i = 0
        while i < len(new_matrix):
            j = 0
            while j < len(new_matrix[0]):
                if new_matrix[i][j] == 1:
                    new_matrix[i][j] += check_lowest_val(i, j, new_matrix)
                j += 1
            i += 1

        max_list = [max(x) for x in new_matrix]
        max_side = max(max_list)
        return max_side ** 2