class Solution:
    def matrixReshape(self, m: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        # O(m*n) T | O(m*n) S        
        m_row,m_col = len(m), len(m[0])
        
        if m_row*m_col!=r*c:
            return m
        
        reshaped = [[]]
        
        for i in range(m_row):
            for j in range(m_col):
                if len(reshaped[-1])==c:
                    reshaped.append([])
                reshaped[-1].append(m[i][j])
        return reshaped
        
        # pythonic
#         flat = sum(m, [])
#         if len(flat) != r * c:
#             return m
#         tuples = zip(*([iter(flat)] * c))
#         return map(list, tuples)
        
        