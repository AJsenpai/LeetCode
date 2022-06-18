class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dynamic programming - bottom up
        
        if not triangle:
            return 
        
        # traversing from second last row of triangle to top
        for row in reversed(range(len(triangle)-1)):
            for col in range(len(triangle[row])): # **
                
                # compare value with its bottom value of left and right
                # triangle = [[11], [9, 10], [7, 6, 10], [4, 1, 8, 3]]
                triangle[row][col] += min(triangle[row+1][col],
                                         triangle[row+1][col+1])
        
        return triangle[0][0]
        