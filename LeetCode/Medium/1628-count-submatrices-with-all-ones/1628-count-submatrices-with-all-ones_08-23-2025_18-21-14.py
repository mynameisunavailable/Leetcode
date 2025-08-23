class Solution:
    def numSubmat(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        result = 0
        firstrow = [0 for x in matrix[0]]
        matrix.insert(0, firstrow)

        #convert matrix to histogram
        for i in range(0, m + 1):
            for j in range(0, n):
                if matrix[i][j] == 1:
                    if matrix[i - 1][j] > 0:
                        matrix[i][j] += matrix[i - 1][j]
        
        #check row by row cell by cell the max matrices
        for i in range(0, m + 1):
            #stack tracks latest height, index, max matrice at that cell
            stack = [[-1, -1, 0]]
            for j in range(0, n):
                while stack[-1][0] > matrix[i][j]:
                    stack.pop(-1)
                matrice_num = matrix[i][j] * (j - stack[-1][1]) + stack[-1][2]
                result += matrice_num
                stack.append([matrix[i][j], j, matrice_num])
        return result