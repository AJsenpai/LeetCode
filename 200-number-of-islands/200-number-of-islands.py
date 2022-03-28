class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col = len(grid), len(grid[0])
        islands = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    islands +=1
                    self.scan(grid,r,c)
        return islands
    
    def scan(self, grid,r,c):
        if r<0 or r>len(grid)-1 or c<0 or c>len(grid[0])-1:
            return
        
        if grid[r][c]!='1':
            return
        
        grid[r][c]=0
        self.scan(grid, r+1,c)
        self.scan(grid, r-1,c)
        self.scan(grid, r,c-1)
        self.scan(grid, r,c+1)
        
        