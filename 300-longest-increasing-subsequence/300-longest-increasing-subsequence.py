class Solution:
    def lengthOfLIS(self, a: List[int]) -> int:
        n = len(a)
        t = [1]*n      
        max_length = 1
        for i in reversed(range(n)):
            for j in range(i+1,n):
                if a[i]<a[j]:
                    t[i] = max(t[i], t[j]+1)
                    max_length = max(max_length, t[i])
        
        return max_length
    
#            for(int i = 0; i < n; i++) 
#             for(int j = 0; j < i; j++) 
#                 if(nums[i] > nums[j]) 
# 				    dp[i] = max(dp[i], dp[j] + 1), ans = max(ans, dp[i]);
#         return ans;
                    
        
        