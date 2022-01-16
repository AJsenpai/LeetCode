class Solution:
    def minSubArrayLen(self, target: int, a: List[int]) -> int:
        # variable size window
        start,end = 0,0
        current_sum = 0 
        length = float('inf')
        while end<len(a):
            current_sum += a[end]
            
            while current_sum >=target:
                length = min(length , end-start+1)
                current_sum -= a[start]
                start += 1
            end += 1
        return length if length < float('inf') else 0
            
        
        