class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S = sum(nums)
        
        if target > S or (S+target)%2!=0:
            return 0
        
        new_target = (sum(nums)-target)//2
        n = len(nums)
        return self.subset_sum_count(nums,new_target,n)
    
    def subset_sum_count(self, a,target,n):
        t = [[-1 for col in range(target+1)] for row in range(n+1)]

        for i in range(n+1):
            for j in range(target+1):
                if i==0:
                    t[i][j] = 0 
                if j==0:
                    t[i][j]=1

        for  i in range(1,n+1):
            for j in range(target+1): # starts from 0 cuz 0 is valid in this question
                if a[i-1]<=j:
                    t[i][j] = t[i-1][j - a[i-1] ] + t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        return t[n][target]
        
        
        
        
        
        