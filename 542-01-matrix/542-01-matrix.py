class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows,cols = len(matrix),len(matrix[0])
        deltas = [(1,0),(-1,0),(0,1),(0,-1)]
            
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
                if (0<=(r+dr) < rows and 
                    0<= (c+dc) < cols and
                    matrix[r][c]+1 < matrix[r+dr][c+dc]                    
                   ):
                    
                    matrix[r+dr][c+dc] = matrix[r][c]+1
                    queue.append((r+dr,c+dc))
        return matrix
                    
                        