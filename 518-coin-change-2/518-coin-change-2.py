class Solution:
    def change(self, target: int, a: List[int]) -> int:
        # unbounded knapsack
        n = len(a)
        
        t = [[-1 for col in range(target+1)] for row in range(n+1)]
        
        for i in range(n+1):
            for j in range(target+1):
                if i==0:
                    t[i][j]= 0
                if j==0:
                    t[i][j]=1
        
        for i in range(1,n+1):
            for j in range(1,target+1):
                if a[i-1]<=j:
                    t[i][j] = t[i][j - a[i - 1]] + t[i - 1][j]
                else:
                    t[i][j] = t[i-1][j]

        return t[-1][-1]
                
        