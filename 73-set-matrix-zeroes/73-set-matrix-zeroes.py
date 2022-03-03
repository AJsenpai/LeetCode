class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        first_row = False
        
        # set first row, first col to 0 if anywhere 
        # we found the zero to keep track of zeroes
        for r in range(row):
            for c in range(col):
                if matrix[r][c]==0:
                    matrix[0][c] = 0 # tracking columns
                    
                    if r>0:
                        matrix[r][0]=0  # tracking rows
                    else:
                        first_row = True # tracking rows 1 cell, overlaped with col
        
        # mark zeroes based on the track we 
        # were keeping 
        for r in range(1,row):
            for c in range(1,col):
                if matrix[0][c]==0 or matrix[r][0]==0: # first col,row iz 0
                    matrix[r][c]=0
        
        # now we need to mark the first row and col
        # which we were using as a tracker to zero
        
        # set entire col zero if first cell is 0
        if matrix[0][0] == 0:        
            for r in range(row):
                matrix[r][0]=0
        
        # set entire row to zero if first row is zero
        if first_row:
            for c in range(col):
                matrix[0][c]=0
        return matrix