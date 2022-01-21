class Solution:
    def mySqrt(self, x: int) -> int:
        # edge case
        if x<=0:
            return 0
        if x==1:
            return 1
        
        start,end = 0,x//2
        
        while start<=end:
            mid = start + (end-start)//2            
            
            square = (mid*mid)
            ceil_square = ((mid+1)*(mid+1))
            
            if square <= x and ceil_square > x:
                return mid
            
            elif  square > x:
                end = mid - 1
            
            elif square < x:                            
                start = mid +1
            
        return -1
    
                    
        