class Solution:
    def searchInsert(self, a: List[int], target: int) -> int:
        start,end=  0,len(a)-1
        while start<=end:
            mid = start+(end-start)//2
            if target == a[mid]:
                return mid
            
            elif target > a[mid]:
                if mid==len(a)-1:
                    return mid + 1
                start = mid + 1
            
            elif target < a[mid]:
                if mid==0 or a[mid-1] < target:
                    return mid
                end = mid -1

            
        