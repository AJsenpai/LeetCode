class Solution:
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        t  = [[-1 for col in range(n+1)] for row in range(m+1)]                 
        t[0][0] = grid[0][0]
        
        for i in range(1,m):
            t[i][0]= t[i-1][0] + grid[i][0]
            
        for j in range(1,n):
            t[0][j]= t[0][j-1]+grid[0][j]
        
        for i in range(1,m):
            for j in range(1,n):
                t[i][j] = grid[i][j] + min(t[i-1][j],t[i][j-1])
        print(t)
        return t[m-1][n-1]
        
#         def solve(grid,m,n):
#             if m==0 or n==0:
#                 return float('inf')
            
#             if m==1 and n==1:
#                 return grid[0][0]
            
#             if t[m][n]!=-1:
#                 return t[m][n]
        
#             t[m][n] = grid[m-1][n-1] + min(solve(grid,m-1,n), solve(grid,m,n-1))
#             return t[m][n]
            
        
        
#         m,n = len(grid),len(grid[0])
#         t  = [[-1 for col in range(n+1)] for row in range(m+1)]        
#         return solve(grid,m,n)
        
        