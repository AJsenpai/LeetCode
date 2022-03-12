class Solution:
    def findMin(self, a: List[int]) -> int:
        if not a or len(a)==1:
            return a[0]
        
        # minimum always lies in the unsorted part
        start,end = 0, len(a)-1
        while start<=end:
            
            mid = (start+end)//2
            
            if mid> start and a[mid-1] > a[mid]:
                return a[mid]
            
            if mid< end and a[mid] > a[mid+1]:
                return a[mid +1]
            
            # go to unsorted part
            if a[start] < a[mid]:
                start = mid+1
            
            else:
                end = mid-1
        
        return a[0] # array not rotated
        