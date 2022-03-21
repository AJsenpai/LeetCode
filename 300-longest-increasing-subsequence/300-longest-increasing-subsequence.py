class Solution:
    def lengthOfLIS(self, a: List[int]) -> int:
        n = len(a)
        t = [1]*n      
        
        for i in reversed(range(n)):
            for j in range(i+1,n):
                if a[i]<a[j]:
                    t[i] = max(t[i], 1+t[j])
        return max(t)
                    
        
        