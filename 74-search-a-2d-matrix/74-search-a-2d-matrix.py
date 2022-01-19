class Solution:
    def searchMatrix(self, a: List[List[int]], target: int) -> bool:
        # start from top right corner
        # we can either go left or go down
        
        # O(m+n) T | O(1) S
        row = 0
        col = len(a[0])-1
        while row < len(a) and col >=0:
            if target < a[row][col]: # go left
                col -= 1
            elif target > a[row][col]: # go down
                row += 1
            else: # target == a[row][col]
                return True
        return False
                
                
                
                
            
        