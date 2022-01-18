class Solution:
    def findMin(self, a: List[int]) -> int:
        if not a:
            return -1
        if len(a) == 1:
            return a[0]
        
        start,end = 0,len(a)-1
        
        while start<=end:
            mid = start + (end-start)//2
            if mid > start  and a[mid-1] > a[mid]:
                return a[mid]
            if mid < end and a[mid] > a[mid+1]:
                return a[mid+1]
            
            if a[start] < a[mid]: # left side is sorted search in right half
                start = mid +1
            else:
                end = mid -1 
        
        return a[0] # array is not rotated 
        
        