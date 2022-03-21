class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1 1 1 1 1 1 1         
        # 1 2 3 4        #  adding values of negative diagonals /
        # 1 3 6 10 ...
        
                
        t = [[1]*n for row in range(m)]
        
        for  i in range(1,m):
            for j in range(1,n):
                t[i][j] = t[i-1][j]+t[i][j-1]
        
        return t[-1][-1]