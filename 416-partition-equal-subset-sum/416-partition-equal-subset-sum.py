class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        arr_sum = sum(nums)
        if arr_sum%2!=0:
            return False
        elif arr_sum%2==0:
            target = arr_sum//2
            t = [[-1 for col in range(target+1)] for row in range(n+1)]
            return self.subsetsum(nums,target,n,t)
    
    def subsetsum(self,a,target,n,t):
        for i in range(n+1):
            for j in range(target+1):
                if i==0:
                    t[i][j] = False
                if j==0:
                    t[i][j] = True
        
        # choices
        for i in range(1,n+1):
            for j in range(1,target+1):
                if a[i-1]<=j:
                    t[i][j] = t[i-1][j-a[i-1]] or t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        return t[n][target]
                    
                
        