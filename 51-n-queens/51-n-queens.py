class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        positive_diagonal = set() # (r+c)
        negative_diagonal = set() #  (r+c)
        result = []
        board = [['.']*n for _ in range(n)]
        self.solve(0, col, n, result, positive_diagonal,negative_diagonal,board)
        return result
    
    def solve(self, r,col,n,result,positive_diagonal,negative_diagonal,board):
        if r==n:
            copy_board = [''.join(row) for row in board]
            result.append(copy_board)
            return 
        
        for c in range(n):
            if c in col or (r+c) in positive_diagonal or (r-c) in negative_diagonal:
                continue
            
            col.add(c)
            positive_diagonal.add(r+c)
            negative_diagonal.add(r-c)
            board[r][c]='Q'
            
            self.solve(r+1,col,n,result,positive_diagonal,negative_diagonal,board)
            
            # backtrack
            col.remove(c)
            positive_diagonal.remove(r+c)
            negative_diagonal.remove(r-c)
            board[r][c]='.'
            