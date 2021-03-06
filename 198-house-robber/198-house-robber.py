class Solution:
    def rob(self, a: List[int]) -> int:
        # fibonacci
        fib1,fib2 = 0,0
        
        for n in a:
            total = max(n+fib1,fib2)
            fib1 = fib2
            fib2 = total
        return total

    # only using t[i-1] and t[i] so we can use two pointers ^
#         n = len(a)
#         t = [0]* (n+1)
#         t[1] = a[0]
        
#         for i in range(1,n):
#             t[i+1] = max(t[i-1]+a[i], t[i])
#         return t[-1]
        

        

            

            
            
                
            