class Solution:
    def findMin(self, a: List[int]) -> int:
        if len(a)==1:
            return a[0]
        
        start,end = 0, len(a)-1
        while start<end: # change
            mid = start + (end-start)//2
            
            if mid > start and a[mid-1] > a[mid]:
                return a[mid]
            
            if mid < end and a[mid]>a[mid+1]:
                return a[mid+1]
            
            if a[mid]==a[start] and a[mid]==a[end]:
                if a[start] > a[start+1]:
                    return a[start+1]
                start += 1
                if a[end-1] > a[end]:
                    return a[end]
                end -= 1
            
            # left is sorted search in right half
            elif a[start] < a[mid] or (a[start]==a[mid] and a[mid] > a[end]):
                start = mid +1
            else:
                end = mid - 1
        return a[0] # array is not rotated
                
                