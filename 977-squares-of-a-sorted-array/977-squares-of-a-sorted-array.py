class Solution:
    def sortedSquares(self, a: List[int]) -> List[int]:
        # two pointers
        if not a:
            return a
        
        result = [0]*len(a)
        left,right = 0,len(a)-1
        
        heighest = len(a)-1
        
        while left <= right:
            leftSqr = a[left]*a[left]
            rightSqr = a[right]*a[right]
            
            if leftSqr > rightSqr:
                result[heighest] = leftSqr
                left += 1
            
            else:
                result[heighest] = rightSqr
                right -= 1
            
            heighest -= 1
        
        return result
    
    
    