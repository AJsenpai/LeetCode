class Solution:
    def minDifference(self, a: List[int]) -> int:
        a.sort()
        
        result = float('inf')
        
        n = len(a)
        i = 0 
        j = n-1-3  # N - 1 is the last element and we want to exlude 3 elements thus n-1-3
        
        while i<=j and j<n:
            result = min(result, a[j]-a[i]) 
            i+=1 
            j+=1
        return result if result != float('inf') else 0
        