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
            
            if  square > x:
                end = mid - 1
            
            elif square < x:
                ceil_square = ((mid+1)*(mid+1))
                if ceil_square > x: # edge case/ we need floor
                    return mid
                start = mid +1
            else:
                return mid
        return -1
    
                    
        