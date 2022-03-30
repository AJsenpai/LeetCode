class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.solve(board,r,c,word,0): # DFS
                    return True
        return False
                    
        
    
    
    def solve(self,board,row,col, word,i):
        if i == len(word): # early check
            return True
        
        if self.oob(board,row,col) or board[row][col]!=word[i]:
            return False
                
                                                       
        char = board[row][col] # found the char
        board[row][col] = '#' # temp mark '#' to avoid visiting again
        
        result =  (self.solve(board, row-1,col,word,i+1) or
            self.solve(board, row+1,col,word,i+1) or
            self.solve(board, row,col-1,word,i+1) or
            self.solve(board, row,col+1,word,i+1)             
           )
            
        board[row][col] = char
            
        return result
                
    
    def oob(self,a,row,col):        
        if row<0 or col < 0 or row >=len(a) or col>=len(a[0]):
            return True
        return False
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
        