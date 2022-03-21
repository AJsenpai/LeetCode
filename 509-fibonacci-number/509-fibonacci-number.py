class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        
        fib1,fib2 = 1,1
        
        for i in range(2,n):
            total = fib1+fib2
            fib1, fib2 = fib2, total
        
        return total