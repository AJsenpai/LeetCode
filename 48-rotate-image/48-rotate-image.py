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
        
        
#         # other technique - rotate single cell at at time
#         for layer in range(0,len(matrix)//2):
#             rotate(matrix,0,len(a)-1-layer)
        
#         def rotate(a,start,end):
#             for i in range(start,end):
#                 temp = a[start][start+i] # save top row val
                
#                 a[start][start+i] = a[end-i][start] # top ==> left
#                 a[end-i][start] = a[end][end-i]     # left ==> bottom
#                 a[end][end-i] = a[start+i][end]     # bottom ==> right
#                 a[start+i][end] = temp              # right ==> top
                
        
        
            
        
        