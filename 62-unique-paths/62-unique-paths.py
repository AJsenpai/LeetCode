class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # start from bottom row, build solution from bottom to top row
        #      10 6 3 1   #  adding values of positive diagonals /
        #       4 3 2 1 
        # 1 1 1 1 1 1 1 
        
        
        t = [[1]*n for row in range(m)]
        
        for  i in range(1,m):
            for j in range(1,n):
                t[i][j] = t[i-1][j]+t[i][j-1]
        
        return t[-1][-1]