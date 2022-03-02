class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # pythonic solution - transpose the matrix and reverse sublist
        
        row = len(matrix)
        col = len(matrix[0])
        
        # transpose, flip row,col = col,row
        for r in range(row):
            for c in range(r, col):
                matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]
        
        for sublist in matrix:
            sublist.reverse()
        # return matrix
            
        
        