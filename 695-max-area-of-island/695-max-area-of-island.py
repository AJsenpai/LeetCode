class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:        
        
        def scan(grid,r,c):            
            if r<0 or c<0 or r> len(grid)-1 or c>len(grid[0])-1:
                return 0
            
            if grid[r][c]==1:
                grid[r][c] = 0
                return (1 + 
                        scan(grid,r+1,c) + 
                        scan(grid,r-1,c) + 
                        scan(grid,r,c-1) + 
                        scan(grid,r,c+1) )
            
            else:
                return 0
        
        row,col = len(grid),len(grid[0])        
        islands = []
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    islands.append(scan(grid,r,c))
        
        return max(islands) if islands else 0
                    
        # return max_island        
                
                
        
        
                    
        