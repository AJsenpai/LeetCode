class Solution:
    def search(self, a: List[int], target: int) -> int:
        start,end = 0,len(a)-1
        
        while start <= end:
            mid = (start+end)//2
            
            if target == a[mid]:
                return mid
            
            elif target < a[mid]:
                end = mid - 1
            
            elif target > a[mid]:
                start = mid+1
        
        return -1
                
        