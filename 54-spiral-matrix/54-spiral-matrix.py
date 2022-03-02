class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:        
        
        output = []
        
        top_row, bottom_row  = 0, len(matrix)-1
        left_col, right_col = 0, len(matrix[0])-1
        
        while top_row<= bottom_row and left_col <= right_col:
            
            # top row
            for i in range(left_col, right_col+1):
                output.append(matrix[top_row][i])
            top_row += 1
            
            # right column
            for i in range(top_row, bottom_row+1):
                output.append(matrix[i][right_col])
            right_col -= 1
            
            # bottom row
            if bottom_row >= top_row:
                for i in reversed(range(left_col,right_col+1)):
                    output.append(matrix[bottom_row][i])
                bottom_row -= 1
            
            # left column
            if left_col <= right_col:
                for i in reversed(range(top_row,bottom_row+1)):
                    output.append(matrix[i][left_col])
                left_col += 1
        
        return output
            
                
        