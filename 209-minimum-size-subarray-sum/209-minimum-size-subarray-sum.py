class Solution:
    def minSubArrayLen(self, target: int, a: List[int]) -> int:
        # variable size window
        start,end = 0,0
        curr_sum = 0
        min_length = float('inf')
        
        while end < len(a):
            curr_sum += a[end]
            
            while curr_sum >=target:
                min_length = min(min_length, end-start+1)                
                curr_sum -= a[start]
                start +=1
            
            end += 1
        return min_length if min_length < float('inf') else 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

            
        
        