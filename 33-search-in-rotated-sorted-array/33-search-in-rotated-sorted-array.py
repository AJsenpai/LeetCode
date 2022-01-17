class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minimum_index= self.findMinimum(nums)
        start,end,right = 0,len(nums)-1,len(nums)-1
        if target<=nums[right]:
            start = minimum_index
        else:
            end= minimum_index-1
        
        while start<=end:
            mid = start+(end-start)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid] :
                end = mid-1
            elif target > nums[mid]:
                start=  mid+1
        return -1
        
        
    def findMinimum(self,a):
        start,end = 0,len(a)-1
        n = len(a)-1
        if a[start]<=a[end]:
            return 0        
        while start<=end:            
            mid = start+(end-start)//2
            mid_prev = (mid-1 + n)%n
            mid_next = (mid+1)%n
            
            if a[mid]<a[mid_prev] and a[mid]<a[mid_next]:
                return mid
            elif a[0] <=a[mid]:
                start = mid + 1
            elif a[-1] > a[mid]:
                end = mid - 1
        return -1
            
        
                
        