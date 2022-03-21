class Solution:
    def rob(self, a: List[int]) -> int:
        # fibonacci,,
        fib1,fib2 = 0,0
        
        for n in a:
            total = max(n+fib1,fib2)
            fib1 = fib2
            fib2 = total
        return total
        

            

            
            
                
            