class Solution:
    def nextGreatestLetter(self, a: List[str], target: str) -> str:
        start,end = 0,len(a)-1
        
        result = None
        while start <= end:
            mid = (start+end)//2
            
            # need to find the next largestletter 
            if target == a[mid]:
                start = mid+1
            
            elif target < a[mid]:
                result = a[mid]
                end = mid-1
            
            elif target > a[mid]:
                start = mid +1
        
        return result if result else a[0]