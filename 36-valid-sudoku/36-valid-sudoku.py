class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        hash = set()
        for r in range(9):
            for c in range(9):
                num = board[r][c]  
                if num!= '.':
                    if (r,num) in hash or (num,c) in hash or (r//3,c//3,num) in hash:
                        return False
                    hash.add((r,num))
                    hash.add((num,c))
                    hash.add((r//3,c//3, num))
        return True
        
        