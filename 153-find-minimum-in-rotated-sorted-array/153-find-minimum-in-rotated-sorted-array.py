class Solution:
    def findMin(self, a: List[int]) -> int:
        if len(a) == 1 or a[0]<a[-1]:
            return a[0]
        start,end = 0,len(a)-1
        right_most = len(a)-1
        while start<=end:
            mid = start + (end-start)//2
            if mid>0 and a[mid-1] > a[mid]:
                return a[mid]
          # search on the right side, because smaller elements are in the right side
            elif a[mid] > a[right_most]:                
                start = mid+1 
            else:
                end =  mid-1
        
        