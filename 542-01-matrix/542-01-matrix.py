class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # BFS
        rows,cols = len(matrix),len(matrix[0])
        deltas = [(1,0),(-1,0),(0,1),(0,-1)] # 4 adjacent directions we can move in
            
        queue = deque()            
        max_dist = max(rows,cols)
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==1:
                    matrix[r][c] = max_dist
                else:
                    queue.append((r,c))
        
        while queue:
            r,c = queue.popleft()
            
            for dr,dc in deltas:
                row,col = r+dr,c+dc                
                if (0<=(row)<rows and 0<=(col)<cols and matrix[r][c]+1 < matrix[row][col]):
                    
                    matrix[row][col] = matrix[r][c]+1
                    queue.append((row,col))
        return matrix
                    
        
                        
            
            
            