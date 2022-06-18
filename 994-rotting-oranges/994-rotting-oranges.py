class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # O(mn) T | O(mn) S
        ROWS,COLS = len(grid),len(grid[0])
        fresh,queue = 0, deque() # fresh, rotten-->queue
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    queue.append((r,c))
        
        mins = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)] # 4 adjacent directions we can move in
        while fresh and queue:
            
            for _ in range(len(queue)):
                r,c = queue.popleft()            
                
                for dr,dc in directions:
                    row,col = dr+r, dc+c
                    if (0<=row<ROWS and 0<=col<COLS and grid[row][col]==1):
                        grid[row][col]=2
                        queue.append((row,col))
                        fresh -=1
                
            mins +=1
                        
        return mins if fresh==0 else -1
            
            
            
            
            
            
            
            
            
            
            
            
            
                
                        
            