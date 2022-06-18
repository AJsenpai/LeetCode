class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # O(mn) T | O(mn) S
        rows,cols = len(grid),len(grid[0])
        fresh,rotten = set(),set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh.add((r,c))
                if grid[r][c]==2:
                    rotten.add((r,c))
        
        mins = 0
        deltas = [(0,1),(0,-1),(1,0),(-1,0)] # 4 adjacent directions we can move in
        while fresh:
            mins +=1
            new_rotten = set()
            
            for r,c in rotten:
                for dr,dc in deltas:
                    if (r+dr,c+dc) in fresh:
                        new_rotten.add((r+dr,c+dc))
            
            if not new_rotten:
                return -1
            rotten = new_rotten
            fresh -= new_rotten # set operation (difference)
        return mins
            
            
            
            
            
            
            
            
            
            
            
            
            
                
                        
            