class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # start from top right corner
        # we can either go left or go down
        
        # O(m+n) T | O(1) S
        row = 0
        col = len(matrix[0])-1
        
        while row < len(matrix) and col >=0:
            if target < matrix[row][col]: # go left
                col -= 1 
            elif target > matrix[row][col]: # go down
                row +=1 
            else:
                return True
        return False