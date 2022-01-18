class Solution:
    def search(self, a: List[int], target: int) -> int:
        start,end = 0,len(a)-1
        while start<=end:
            mid = start + (end-start)//2
            
            if a[mid]==target:
                return mid
            
            # check which part is sorted in ascending order
            # compare the target with sorted range
            if a[start] <= a[mid]: # left is sorted ascending 
                if target >= a[start] and target < a[mid]: 
                    # target is in the left range
                    end = mid - 1
                else: # target in unsorted range
                    start = mid +1
            else: # right is sorted
                if target <= a[end] and target > a[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
                    
                
            
                
            
        