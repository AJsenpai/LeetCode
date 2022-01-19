class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        if len(a)==1:
            return 0
        
        start,end = 0,len(a)-1
        while start<=end:
            # left | mid | right
            mid = start + (end-start)//2
            
            if mid > 0 and mid<len(a)-1:
                if a[mid] > a[mid-1] and a[mid] > a[mid+1]:
                    return mid
                elif a[mid-1] > a[mid]:
                    end = mid - 1
                elif a[mid+1] > a[mid]:
                    start = mid +1
            else:
                if mid==0:
                    if a[0] > a[1]:
                        return 0
                    else:
                        return 1
                
                elif mid==len(a)-1:
                    if a[len(a)-1] > a[len(a)-2]:
                        return len(a)-1
                    else:
                        return len(a)-2
                        
                    
            
        