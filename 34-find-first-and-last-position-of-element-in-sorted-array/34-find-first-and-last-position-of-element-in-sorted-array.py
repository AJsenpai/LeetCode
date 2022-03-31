class Solution:
    def searchRange(self, a: List[int], target: int) -> List[int]:
            if not a:
                return [-1,-1]
            
            result = [-1, -1]
            result[0] = self.binarysearch(a,target,False)        
            
            if result[0] != -1:
                result[1] = self.binarysearch(a,target,True)
            
            return result
        
    def binarysearch(self, a,target,firstOccurrence):            
        targetIdx = -1
        start,end = 0, len(a)-1

        while start<=end:
            mid = start + (end-start)//2

            if target < a[mid]:
                end = mid-1
                
            elif target > a[mid]:
                start = mid+1
                
            else:                
                targetIdx = mid                    
                if firstOccurrence:
                    start = mid+1
                else:
                    end = mid-1                

        return targetIdx



