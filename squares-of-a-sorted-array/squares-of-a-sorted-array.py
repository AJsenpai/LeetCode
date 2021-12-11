class Solution:
    def sortedSquares(self, a: List[int]) -> List[int]:
        if not a :
            return a
        start,end = 0,len(a)-1
        squares = [0]*len(a)
        
        highest = len(squares)-1
        while start<=end:
            sq1 = a[start]*a[start]
            sq2 = a[end]*a[end]
            if sq1>sq2:
                squares[highest] = sq1
                start += 1
            else:
                squares[highest] = sq2
                end -= 1
            highest -=1
            
        return squares
                