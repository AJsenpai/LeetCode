class Solution:
    def nextGreatestLetter(self, a: List[str], target: str) -> str:
        if target >= a[-1]: # greater than last char, edgecase
            return a[0]
        
        
        start,end = 0,len(a)-1        
        result = 0
        while start <= end:
            mid = (start+end)//2
            
            # need to find the next largestletter 
            if a[mid] <= target:
                start = mid +1
            elif a[mid] > target:
                result = a[mid]
                end = mid-1
                
        return result