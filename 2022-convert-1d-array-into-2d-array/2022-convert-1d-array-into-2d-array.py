class Solution:
    def construct2DArray(self, a: List[int], m: int, n: int) -> List[List[int]]:
        if len(a) != m*n:
            return
        
        td = [[0 for col in range(n)] for row in range(m)]
        
        idx=0
        
        for i in range(m):
            for j in range(n):
                td[i][j] = a[idx]
                idx+=1
        return td
            