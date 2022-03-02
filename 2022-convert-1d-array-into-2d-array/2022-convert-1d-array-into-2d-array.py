class Solution:
    def construct2DArray(self, a: List[int], m: int, n: int) -> List[List[int]]:
        # m = row 
        # n = col
        if len(a) != m*n:
            return
        
        td = [[0 for col in range(n)] for row in range(m)]
        
        idx=0
        
        for i in range(m): # row 
            for j in range(n): # col
                td[i][j] = a[idx]
                idx+=1
        return td
            