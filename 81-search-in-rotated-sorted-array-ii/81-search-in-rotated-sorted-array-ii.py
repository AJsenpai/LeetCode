class Solution:
    def search(self, a: List[int], target: int) -> bool:
        # if len(a)==1:
        #      return target==a[0]
            
            
        start,end = 0,len(a)-1
        while start<= end:
            mid = start+(end-start)//2
            if a[mid]==target:
                return True
            
            if a[start]==a[mid] and a[end]==a[mid]:
                start += 1
                end -= 1
            
            elif a[start] <= a[mid]: # left is sorted
                if target >= a[start] and target < a[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= a[end] and target > a[mid]:
                    start = mid + 1
                else:
                    end = mid -1 
        return False

        