class Solution:
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def solve(grid,m,n):
            if m==0 or n==0:
                return float('inf')
            
            if m==1 and n==1:
                return grid[0][0]
            
            if t[m][n]!=-1:
                return t[m][n]
        
            t[m][n] = grid[m-1][n-1] + min(solve(grid,m-1,n), solve(grid,m,n-1))
            return t[m][n]
            
        
        
        m,n = len(grid),len(grid[0])
        t  = [[-1 for col in range(n+1)] for row in range(m+1)]        
        return solve(grid,m,n)
        
        