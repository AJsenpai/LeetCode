class Solution:
    def peakIndexInMountainArray(self, a: List[int]) -> int:
        start,end = 0, len(a)-1
        
        while start<=end:
            mid = (start+end)//2
            left = a[mid-1] if mid> 0 else float('-inf')
            right = a[mid+1] if mid < len(a)-1 else float('inf')
            
            
            if left > a[mid] and right <a[mid]:
                end = mid-1
            elif left < a[mid] and right > a[mid]:
                start = mid+1
            elif left > a[mid] and right > a[mid]:
                start = mid+1
            else:
                return mid
        return -1
        