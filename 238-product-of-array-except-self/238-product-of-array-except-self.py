class Solution:
    def productExceptSelf(self, a: List[int]) -> List[int]:
        n = len(a)        
        result = [1]*n
        
        # calculate prefix product
        prefix = 1 
        for i in range(n):
            result[i] = prefix 
            prefix *= a[i]  # for next i 
        
        postfix = 1
        for i in reversed(range(n)):
            result[i] *= postfix
            postfix *= a[i] # for next i-1
        
        return result
            
            
